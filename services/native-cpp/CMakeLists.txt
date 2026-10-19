cmake_minimum_required(VERSION 3.20)
project(acme_img CXX)

set(CMAKE_CXX_STANDARD 17)

add_library(img src/resizer.cpp)
target_include_directories(img PUBLIC include)

add_executable(resize_demo src/main.cpp)
target_link_libraries(resize_demo img)

enable_testing()
add_executable(resize_test src/resize_test.cc)
target_link_libraries(resize_test img)
add_test(NAME resize_test COMMAND resize_test)
