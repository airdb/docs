#!/bin/bash

cd $(dirname $0) || exit 1

function main()
{
  for i  in build  CMakeCache.txt  CMakeFiles  cmake_install.cmake Makefile; 
  do 
    find . -name $i | xargs -i rm -rf {} \;
  done
}

main "$@"
