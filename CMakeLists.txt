cmake_minimum_required(VERSION 3.10)

project(MyProject C)

set(CMAKE_C_COMPILER gcc)

file(GLOB SOURCES "System/*.c" "main.c")

add_executable(FileManager ${SOURCES})

target_include_directories(FileManager PRIVATE System/include)

target_link_libraries(FileManager PRIVATE gdi32 user32)

