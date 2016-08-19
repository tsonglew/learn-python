#!/bin/sh

array1=(1 2 3 4 5)
array2=(
1
2
3
4
5
)
echo ${array1[0]}
echo 'array2'
# @ to get all elements
echo ${array2[@]}
# length of the array
echo ${#array2[@]}
echo ${#array2[*]}
# length of an element
echo ${#array2[0]}
