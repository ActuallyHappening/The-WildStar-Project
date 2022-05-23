#include <Arduino.h>
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
#ifdef IMPLEMENTATION
  println(prefix, message);
#endif
}
void info(char *prefix, char *message)
{
#ifdef INFO
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
  __debug__->save("test");
  __debug__->save("{'__debug__': '" + message + "','__version':'v0.0.1'}"); // SCAN VERSION
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