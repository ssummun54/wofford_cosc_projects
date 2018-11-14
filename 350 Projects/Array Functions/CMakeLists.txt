cmake_minimum_required(VERSION 3.8)
project(Array_Functions)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp arrayfunctions.cpp arrayfunctions.h)
add_executable(Array_Functions ${SOURCE_FILES})

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")