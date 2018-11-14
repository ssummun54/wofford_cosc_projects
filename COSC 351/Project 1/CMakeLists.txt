cmake_minimum_required(VERSION 3.8)
project(Assignment_1)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c)
add_executable(Assignment_1 ${SOURCE_FILES})

set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")