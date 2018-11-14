cmake_minimum_required(VERSION 3.8)
project(Project_5)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp circularqueue.h)
add_executable(Project_5 ${SOURCE_FILES})

set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")