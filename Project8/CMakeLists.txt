cmake_minimum_required(VERSION 3.8)
project(Project08)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp sudoku.cpp sudoku.h sudokusolver.cpp sudokusolver.h)
add_executable(Project08 ${SOURCE_FILES})
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")