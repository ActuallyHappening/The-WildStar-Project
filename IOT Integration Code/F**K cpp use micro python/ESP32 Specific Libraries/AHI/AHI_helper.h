#include <Arduino.h>
//#define IMPLEMENTATION
//#define DEBUG
//#define INFO
//#define DEBUG_REMOTE
void print(char *message)
{
#ifndef DONT_USE_SERIAL
  Serial.print(message);
#endif
}
void println(char *prefix, char *message)
{
  print(prefix);
  print((char *)" ");
  print(message);
  print((char *)"\n");
}
void implementation(char *prefix, char *message)
{
  // Serial.println("^^^ DEBUG IMPLEMENTATION ^^^");
#ifdef IMPLEMENTATION
  // Serial.println("^^ DEBUG IMPLEMENTATION ^^");
  println(prefix, message);
#endif
}
void info(char *prefix, char *message)
{
  // Serial.println("^^^ DEBUG INFO ^^^");
#ifdef INFO
  // Serial.println("^^ DEBUG INFO ^^");
  println(prefix, message);
#endif
}
void debug(char *prefix, char *message)
{
#ifdef DEBUG
  println(prefix, message);
#endif
}

void debug_remote(char *message)
{
#ifndef DONT_USE_AIO
#ifdef DEBUG_REMOTE
  debug((char *)"(AIO DEBUG_REMOTE)", (char *)"Sending following debug message through AIO ...");
  debug((char *)"(AIO DEBUG_REMOTE)", message);
  __debug__->save((char *)"test");
  __debug__->save((char *)"{'__debug__': '" + message + (char *)"','__version':'v0.0.1'}"); // SCAN VERSION
#endif
#endif
}
int debug_remote(char *message, int current, int max)
{
  if (current < max)
  {
    debug_remote(message);
    return current + 1;
  }
  else
  {
    return 0;
  }
}