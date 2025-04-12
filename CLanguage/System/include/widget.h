#ifndef WIDGET_H
#define WIDGET_H

#define MAX_ID_LENGTH 100

typedef struct Widget {
    int width, height;
    int border_size, border_radius;
    int color;
    int howered;
    int on_click;
    struct Widget** children;
    char id[MAX_ID_LENGTH];
} Widget;

Widget create_widget(int width, int height, int color, const char id[MAX_ID_LENGTH]);

#endif // WIDGET_H