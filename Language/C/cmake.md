cmake简单使用
===

1. 
cat helloworld.c 
#include <stdio.h>

int main(int argc, char *argv[])
{
  printf("hello world\n");
  return 0;
}


2. 
cat CMakeLists.txt 
project(HELLOWORLD)
set(SRC_LIST helloworld.c)
add_executable(helloworld ${SRC_LIST})


tree 
.
├── CMakeLists.txt
└── helloworld.c

0 directories, 2 files



3. 

cmake  .
-- The C compiler identification is GNU 4.8.2
-- The CXX compiler identification is GNU 4.8.2
-- Check for working C compiler: /bin/cc
-- Check for working C compiler: /bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /bin/c++
-- Check for working CXX compiler: /bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /root/tmp/helloword


tree 
.
├── CMakeCache.txt
├── CMakeFiles
│   ├── 2.8.11
│   │   ├── CMakeCCompiler.cmake
│   │   ├── CMakeCXXCompiler.cmake
│   │   ├── CMakeDetermineCompilerABI_C.bin
│   │   ├── CMakeDetermineCompilerABI_CXX.bin
│   │   ├── CMakeSystem.cmake
│   │   ├── CompilerIdC
│   │   │   ├── a.out
│   │   │   └── CMakeCCompilerId.c
│   │   └── CompilerIdCXX
│   │       ├── a.out
│   │       └── CMakeCXXCompilerId.cpp
│   ├── cmake.check_cache
│   ├── CMakeDirectoryInformation.cmake
│   ├── CMakeOutput.log
│   ├── CMakeTmp
│   ├── helloworld.dir
│   │   ├── build.make
│   │   ├── cmake_clean.cmake
│   │   ├── DependInfo.cmake
│   │   ├── depend.make
│   │   ├── flags.make
│   │   ├── link.txt
│   │   └── progress.make
│   ├── Makefile2
│   ├── Makefile.cmake
│   ├── progress.marks
│   └── TargetDirectories.txt
├── cmake_install.cmake
├── CMakeLists.txt
├── helloworld.c
└── Makefile

6 directories, 28 files


5.

make 
Scanning dependencies of target helloworld
[100%] Building C object CMakeFiles/helloworld.dir/helloworld.c.o
Linking C executable helloworld
[100%] Built target helloworld

ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  CMakeLists.txt  helloworld  helloworld.c  Makefile


6.
./helloworld 
hello world
