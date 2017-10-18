#!/bin/bash

echo "Input a:"
read a
echo "Input b:"
read b

#if [ $a -eq $b ]
if (( $a == $b ))
then
echo "a ($a) ir vienāds b ($b)"
#elif [ $a -gt $b ]
elif (( $a > $b ))
then
echo "a ($a) ir lielāks par b ($b)"
else
echo "a ($a) ir mazāks par b ($b)"
fi




: <<'END'
if [ $a -gt $b ]
then
echo "a ($a) > b ($b)"
else
echo "nē a ($a) nav lielāks par b ($b)"
fi
END
