// This is NOT my code!

/************************ Adafruit IO Config *******************************/

// visit io.adafruit.com if you need to create an account,
// or if you need your Adafruit IO key.

#include <Arduino.h>

#include "AHI_Secrets.plsgitignore.h"

#ifndef DONT_USE_AIO
#include "AdafruitIO_WiFi.h"

AdafruitIO_WiFi io(AIO_SECRET_USERNAME, AIO_SECRET_KEY, WIFI_SECRET_SSID, WIFI_SECRET_PASSWORD);

AdafruitIO_Feed *__debug__ = io.feed("embedded.embedded-test");
#endif

#define LOCAL_ID 1 // Like mac address but for only my IOT things