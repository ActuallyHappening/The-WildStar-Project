// This is NOT my code!

/************************ Adafruit IO Config *******************************/

// visit io.adafruit.com if you need to create an account,
// or if you need your Adafruit IO key.

#include "AHI_Secrets.plsgitignore.h"

#define IO_USERNAME AIO_SECRET_USERNAME
#define IO_KEY AIO_SECRET_KEY

#define WIFI_SSID WIFI_SECRET_SSID
#define WIFI_PASS WIFI_SECRET_PASSWORD

#ifndef DONT_USE_AIO
#include "AdafruitIO_WiFi.h"

AdafruitIO_WiFi io(IO_USERNAME, IO_KEY, WIFI_SSID, WIFI_PASS);

AdafruitIO_Feed *__test__ = io.feed("embedded.embedded-test");
#endif

#define LOCAL_ID 1 // Like mac address but for only my IOT things