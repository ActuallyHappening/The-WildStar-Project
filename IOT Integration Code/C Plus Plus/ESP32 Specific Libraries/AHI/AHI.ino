#define VERSION_WARNINGS

#ifdef VERSION_WARNINGS
#define AHI_VERSION "0.0.1" // SCAN VERSION
#warning AHI.ino version: 0.0.1 // SCAN VERSION
#endif

#define IMPLEMENTATION
#define INFO
#define DEBUG
#define DEBUG_REMOTE 100 // Means posting many unnecessary and slow debug messages over the air, 100 being every 100 ticks

#define REMOTE_CONTROL         // Means allowing remote control
#define USE_AHI_DYNAMIC        // Means reassigning gpio pins
#define USE_AHI_DYNAMIC_REMOTE // Means being able to reassign gpio pins

//#define DONT_USE_SERIAL
//#define DONT_USE_AIO
#define DONT_USE_IR_SENDER
#define DONT_USE_IR_RECEIVER

#include <Arduino.h>

#include "AHI_localConfig.h"
#include "AHI_helper.h"

#define IRCODES_INCLUDE_CANDLE

#include <IRcodes.h>

#include <IRremote.hpp>

#ifdef DEBUG_REMOTE
int debugFrameCounter = DEBUG_REMOTE;
#endif

void setup()
{
#ifndef DONT_USE_SERIAL
  Serial.begin(115200);
  // while (!Serial) {;}
  implementation((char *)"(IMPLEMENTATION)", (char *)"@@ BEGIN AHI.ino setup @@");
  println((char *)"(*SERIAL)", (char *)"Serial beginning in AHI.ino ...");
#endif
#ifndef DONT_USE_AIO
  AdafruitIO_Feed *PutFeed = io.feed("embedded.embedded-in-test");
  AdafruitIO_Feed *GetFeed = io.feed("embedded.embedded-to-test");
  io.connect();

  println((char *)"(*AIO)", (char *)"Connecting to Adafruit IO ...");

  while (io.status() < AIO_CONNECTED)
  {
    Serial.print(F("."));
    delay(420);
  }

#ifndef DONT_USE_SERIAL
  print((char *)"(*AIO) * Connected to Adafruit IO *");
  Serial.println(io.statusText());
  // println("(*AIO)", io.statusText()); // Need to convert from__flashStringHelper
  //  See https://forum.arduino.cc/t/convert-flash-string-to-char/564927
#endif
#endif
  implementation((char *)"(IMPLEMENTATION)", (char *)"@@ END AHI.ino setup @@");
}

void loop()
{
  implementation((char *)"(IMPLEMENTATION)", (char *)"@@ LOOP AHI.ino loop @@");
  Serial.println("Loop: " + String(debugFrameCounter));
#ifndef DONT_USE_AIO
  io.run();
  debugFrameCounter = debug_remote((char *)"Looping ...", debugFrameCounter, DEBUG_REMOTE);
#endif
}

void _handleAIO_TO(AdafruitIO_Data *data)
{
  print((char *)"(*AIO) & Message received: ");
  print(data->value());
  print((char *)" & \n");
}