cmake_minimum_required(VERSION 2.8)
PROJECT(HELLO)

# 添加工程子目录, 子目录下必须要有CMakeLists.txt文件
MESSAGE(STATUS "==Dean== This is SOURCE dir "${HELLO_SOURCE_DIR}/src)
ADD_SUBDIRECTORY(./src)
