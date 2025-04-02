cmake_minimum_required(VERSION 3.10)

# Projekt
project(MyProject C)

# Ustawienie kompilatora
set(CMAKE_C_COMPILER gcc)

# Dodanie plików źródłowych
file(GLOB SOURCES "System/*.c" "main.c")

# Utworzenie pliku wykonywalnego
add_executable(FileManager ${SOURCES})

# Zdefiniowanie katalogu nagłówków, jeśli masz dodatkowe pliki nagłówkowe
target_include_directories(FileManager PRIVATE System/include)

# Linkowanie bibliotek Windowsa (w tym GDI)
target_link_libraries(FileManager PRIVATE gdi32 user32)

# Możesz dodać inne biblioteki, jeśli ich używasz, np. opengl32, comdlg32, itd.
