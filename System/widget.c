#include <widget.h>
#define MAX_ID_LENGTH 100

typedef struct {
  int width, height;
  int border_size, border_radius;

  int color;

  int howered;
  int on_click;

  Widget** children;
  char id[100];
} Widget;



