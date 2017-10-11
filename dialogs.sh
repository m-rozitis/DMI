#!/bin/bash

echo "Cienijamais lietotāj, lūdzu ievadīt pirmo argumentu: "
read a
echo "Cienijamais lietotāj, lūdzu ievadīt otro argumentu: "
read b
sum=`expr $a + $b`
echo "$a + $b = "$sum
starp=`expr $a - $b`
echo "$a - $b = "$starp
reiz=`expr $a \* $b`
echo "$a * $b = "$reiz
dal=`expr $a / $b`
echo "$a / $b = "$dal
atl=`expr $a % $b`
echo "$a % $b = "$atl
