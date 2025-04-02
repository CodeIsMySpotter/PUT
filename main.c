#include <windows.h>
#include <window.h>

int main() {
    Window win;
    
    if (createWindow(&win, "My Window", 0.8, 0.8) != 0) {
        return -1;
    }

    ShowWindow(win.hwnd, SW_SHOW);
    UpdateWindow(win.hwnd);
    startEventLoop(&win);
    destroyWindow(&win);

    return 0;
}