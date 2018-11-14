cmake_minimum_required(VERSION 3.8)
project(ListADT_LinkedImplementation)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp list.cpp list.h)
add_executable(ListADT_LinkedImplementation ${SOURCE_FILES})
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")