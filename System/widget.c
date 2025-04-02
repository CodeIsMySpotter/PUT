  #include <widget.h>

  typedef struct {
    int width, height;
    int border_size, border_radius;

    int color;

    int howered;
    int on_click;

    Widget** children;
    char id[MAX_ID_LENGTH];
  } Widget;


  Widget create_widget(int width, int height, int color, char id[MAX_ID_LENGTH]) {
    return Widget {
      width, height,
      NULL, NULL,
      color,
      NULL,
      NULL,
      NULL
      id
    };
  }
