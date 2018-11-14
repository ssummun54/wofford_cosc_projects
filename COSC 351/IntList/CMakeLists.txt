cmake_minimum_required(VERSION 3.8)
project(Project4)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp intlist.cpp intlist.h)
add_executable(Project4 ${SOURCE_FILES})
set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")