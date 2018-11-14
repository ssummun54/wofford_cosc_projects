cmake_minimum_required(VERSION 3.8)
project(List_ADT_Project)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp list.cpp list.h)
add_executable(List_ADT_Project ${SOURCE_FILES})
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")