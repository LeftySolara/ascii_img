cmake_minimum_required(VERSION 2.8)
project(AsciiArt)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(AsciiArt main.cpp)
target_link_libraries(AsciiArt ${OpenCV_LIBS})