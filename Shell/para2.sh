#!/bin/sh

echo "Shell parameters:";
echo "para1: $0";
echo "para2: $1";
echo "number of the arguments: $#";
echo "display arguments as the first string: $*";
echo "current process id: $$";
echo "last process id in the backend: $!";
