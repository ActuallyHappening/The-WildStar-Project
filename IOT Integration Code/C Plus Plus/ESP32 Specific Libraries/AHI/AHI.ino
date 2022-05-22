#define VERSION_WARNINGS

#ifdef VERSION_WARNINGS
#define AHI_VERSION "0.0.1" // SCAN VERSION
#warning AHI.ino version: AHI_VERSION
#endif

#define IMPLEMENTATION
#define INFO
#define DEBUG
#define DEBUG_REMOTE // Means posting many unnecessary and slow debug messages over the air

#define POST_STATUS_REMOTE     // Means posting (unnecessary) status updates over the air
#define USE_AHI_DYNAMIC        // Means reassigning gpio pins
#define USE_AHI_DYNAMIC_REMOTE // Means being able to reassign gpio pins

//#define DONT_USE_SERIAL
//#define DONT_USE_AIO
#define DONT_USE_IR_SENDER
#define DONT_USE_IR_RECEIVER

#include <Arduino.h>

#include "AHI_localConfig.h"

#define IRCODES_INCLUDE_CANDLE

#include <IRcodes.h>

#include <IRremote.hpp>

void setup()
{
#ifndef DONT_USE_SERIAL
  Serial.begin(115200);
// while (!Serial) {;}
#ifdef IMPLEMENTATION
  Serial.println(F("(IMPLEMENTATION) @@ BEGIN AHI.ino setup @@"));
#endif
  Serial.println(F("(*SERIAL) Serial beginning in AHI.ino ..."));
#endif
#ifndef DONT_USE_AIO
  AdafruitIO_Feed *IN__test__ = io.feed("embedded.embedded-in-test");
  AdafruitIO_Feed *TO__test__ = io.feed("embedded.embedded-to-test");
  io.connect();

#ifndef DONT_USE_SERIAL
  Serial.println(F("(*AIO) Connecting to Adafruit IO ..."));
#endif

  while (io.status() < AIO_CONNECTED)
  {
    Serial.print(F(". "));
    delay(42);
  }

#ifndef DONT_USE_SERIAL
  Serial.print(F("(*AIO) * Connected to Adafruit IO *"));
  Serial.print(io.statusText());
#endif
#endif

#ifndef DONT_USE_SERIAL
#ifdef IMPLEMENTATION
  Serial.println(F("(IMPLEMENTATION) @@ END AHI.ino setup @@"));
#endif
#endif
}

void loop()
{
#ifdef IMPLEMENTATION
#ifndef DONT_USE_SERIAL
  Serial.println(F("(IMPLEMENTATION) @@ LOOP AHI.ino loop @@"));
#endif
#endif
#ifndef DONT_USE_AIO
  io.run();
#ifdef DEBUG_REMOTE
#ifndef DONT_USE_SERIAL
  Serial.println("(AIO DEBUG_REMOTE) Sending debug message through AIO ...");
#endif
  __test__->save(F('{"__metaversion__":"0.1.0","meta_structure":"EMBEDDED DEBUG_REMOTE", "payload":{"position":"AHI.ino :: loop"}}'));
#endif
#endif
}

void _handleAIO_TO(AdafruitIO_Data *data)
{
#ifndef DONT_USE_SERIAL
  Serial.print(F("(*AIO) & Message received: "));
  Serial.print(data->value());
  Serial.println(F(" & "));
#endif
}