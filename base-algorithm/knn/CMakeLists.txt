cmake_minimum_required(VERSION 3.5)
project(knn)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp kd_tree.cpp kd_tree.h)
add_executable(knn ${SOURCE_FILES})