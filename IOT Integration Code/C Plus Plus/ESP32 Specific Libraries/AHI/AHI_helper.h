#include <Arduino.h>
void print(char *message);
void println(char *prefix, char *message);
void implementation(char *prefix, char *message);
void info(char *prefix, char *message);
void debug(char *prefix, char *message);

void debug_remote(char *message);
int debug_remote(char *message, int current, int max);