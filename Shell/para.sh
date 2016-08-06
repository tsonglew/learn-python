#!/bin/sh

your_name="kasheemlew"
echo $your_name
# brace is optional
echo ${your_name}

for i in `ls /etc`; do
    echo " ${i}"
done

# reassign would cast an error
readonly your_name
# your_name="k"

# delete an parameter
unset your_name

str='this \n is a \n string'
echo $str
str="this \n is a \n string"
echo $str

string="abcd"
# get the length of the string
echo ${#string}
string="hello world!"
# get from index 1 to index 4
echo ${string:1:4}
# find index world
echo `expr index "$string" world`
