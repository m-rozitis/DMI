#!/bin/bash

echo "Input a:"
read a
echo "Input b:"
read b
echo "Input c:"
read c


#if [ $a -eq $b -eq $b ]
if (( $a == $b == $c ))
then
echo "a ($a) ir vienāds b ($b) ir vienāds c ($c)"
#elif [ $a -gt $b ]
elif (( $a > $b > $c ))
then
echo "a ($a) ir lielāks par b ($b) un c ($c)"
else
echo "a ($a) ir mazāks par b ($b) un c ($c)"
fi




: <<'END'
if [ $a -gt $b ]
then
echo "a ($a) > b ($b)"
else
echo "nē a ($a) nav lielāks par b ($b)"
fi
END
