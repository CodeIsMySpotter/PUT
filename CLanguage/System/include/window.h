#ifndef WINDOW_H
#define WINDOW_H

#include <windows.h>

typedef struct {
    HWND hwnd;      
    HDC hdc;        
} Window;


int createWindow(Window* win, const char* title, float width, float height);
void setCenter(HWND hwnd);
void destroyWindow(Window* win);
void startEventLoop();
#endif 
