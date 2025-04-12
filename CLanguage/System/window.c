#include <window.h>
#include <stdio.h>
#include <stdlib.h>

/// Window Procedure Function to handle window messages.
static LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_DESTROY:
            PostQuitMessage(0);  ///< Post a message to quit the application.
            break;

        case WM_PAINT:
            // Handle window painting (currently empty).
            break;

        case WM_MOUSEMOVE:
            SetCursor(LoadCursor(NULL, IDC_ARROW));  ///< Change cursor to arrow on mouse move.
            break;

        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);  ///< Default window procedure for unhandled messages.
    }
    return 0;
}

/// Function to create a window and initialize necessary components.
/// @param win - Pointer to a Window structure.
/// @param title - Window title as a string.
/// @param width - Width of the window as a fraction of screen width.
/// @param height - Height of the window as a fraction of screen height.
/// @return - Returns 0 on success, or -1 on failure.
int createWindow(Window* win, const char* title, float width, float height) {
    
    int X, Y;
    X = GetSystemMetrics(SM_CXSCREEN);  ///< Get screen width.
    Y = GetSystemMetrics(SM_CYSCREEN);  ///< Get screen height.
    
    // Check if window dimensions are valid.
    if(width <= 0 || height <= 0 || X*width > X || Y*height > Y) {
        return -1;  ///< Return error if dimensions are invalid.
    }

    WNDCLASS wc = {0};  ///< Initialize window class.
    wc.lpfnWndProc = WindowProc;  ///< Set the window procedure function.
    wc.hInstance = GetModuleHandle(NULL);  ///< Get current module handle.
    wc.lpszClassName = "FileManager";  ///< Set window class name.

    // Register window class.
    if (!RegisterClass(&wc)) {
        MessageBox(NULL, "[ERROR] :: Window Class registration failed", "Error", MB_OK | MB_ICONERROR);
        return -1;  ///< Return error if registration fails.
    }

    // Create the window.
    win->hwnd = CreateWindowEx(
        0, "FileManager", title, WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, X*width, Y*height,
        NULL, NULL, wc.hInstance, NULL);

    if (!win->hwnd) {
        MessageBox(NULL, "[ERROR] :: Window creation failed", "ERROR", MB_OK | MB_ICONERROR);
        return -1;  ///< Return error if window creation fails.
    }

    // Set the cursor to the default arrow.
    SetCursor(LoadCursor(NULL, IDC_ARROW));
    
    // Get device context (HDC) for drawing on the window.
    HDC hdc = GetDC(win->hwnd);

    // Center the window on the screen.
    setCenter(win->hwnd);

    return 0;  ///< Return success.
}

/// Function to center the window on the screen.
/// @param hwnd - Handle to the window to be centered.
void setCenter(HWND hwnd) {
    
    RECT windowRect;
    GetWindowRect(hwnd, &windowRect);  ///< Get the window's dimensions.
    int windowWidth = windowRect.right - windowRect.left;
    int windowHeight = windowRect.bottom - windowRect.top;

    RECT screenRect;
    SystemParametersInfo(SPI_GETWORKAREA, 0, &screenRect, 0);  ///< Get the work area (excluding taskbar).

    // Calculate the center position.
    int centerX = (screenRect.right - screenRect.left - windowWidth) / 2 + screenRect.left;
    int centerY = (screenRect.bottom - screenRect.top - windowHeight) / 2 + screenRect.top;

    // Set the window's position to the center.
    SetWindowPos(hwnd, HWND_TOP, centerX, centerY, 0, 0, SWP_NOSIZE);
}

/// Function to clean up and destroy the window and its resources.
/// @param win - Pointer to a Window structure to be destroyed.
void destroyWindow(Window* win) {
    ReleaseDC(win->hwnd, win->hdc);  ///< Release the device context.
    DestroyWindow(win->hwnd);  ///< Destroy the window.
}

/// Function to start the event loop for processing messages.
/// The loop continues until the application is closed.
void startEventLoop() {
    MSG msg;

    // Process messages in the event loop.
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);  ///< Translate virtual-key messages into character messages.
        DispatchMessage(&msg);   ///< Dispatch the message to the window procedure.
    }
}
