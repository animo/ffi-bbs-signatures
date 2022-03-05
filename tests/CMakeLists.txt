cmake_minimum_required(VERSION 3.10)

project(bbs_test LANGUAGES C)

add_executable(bbs_test bbs_test.c)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY .)

target_include_directories(bbs_test PUBLIC "../include")

file(GLOB LIBRARIES "../target/release/libbbs.dylib")

target_link_libraries(bbs_test PUBLIC "${LIBRARIES}")
