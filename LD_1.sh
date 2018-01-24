#!/bin/bash

echo -n "Lietotāj, lūdzu, ievadi skaitli: "
read x

echo -e "x  |\t%1|\t%2|\t%3|\t%4|\t%5|\t%10"
echo "---------------------------------------------------"

k=0

while (($k<10))
do

s1=`expr $x % 1`
s2=`expr $x % 2`
s3=`expr $x % 3`
s4=`expr $x % 4`
s5=`expr $x % 5`
s10=`expr $x % 10`

echo -e "$x |\t$s1 |\t$s2 |\t$s3 |\t$s4 |\t$s5 |\t$s10"
#echo "-----------------------------------------"

k=`expr $k + 1`
x=`expr $x + 1`
done

