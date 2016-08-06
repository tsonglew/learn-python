#!/bin/sh

val=`expr 2 + 2`  # must with space between numbers and +
echo "sum: $val"

val=`expr 2 \* 2`  # \ before *
echo "multiply: $val"

a=10
b=20
# if...then...fi
if [ $a == $b ]
then
    echo "a is equal to b"
fi

# and(&&)
if [ $a -gt $b -a $a -lt $b ]
then
    echo "somthing..."
fi

# or(||)
if [ $a -le $b -o $a -ne $b ]
then
    echo "something..."
else
    echo "something else"
fi

# Sentence
# [ $a = $b ]: sentence a is equal to sentence b
# [ $a != $b ]: sentence a is not equal to sentence b
# [ -z $a ]: length is 0
# [ -n $a ]: length is not 0
# [ $a ]: sentence is None
