#!/bin/bash
echo "Lietotāj, lūdzu, ievadi skaitļus: "
read input
a=($input)

n=${#a[@]}

sort=($(printf "%s\n" "${a[@]}" | sort -n))
echo ${sort[@]}
echo "Lielākais skaitlis ir " ${sort[0]}
echo "Mazākais skaitlis ir " ${sort[n-1]}

if (( n % 2 == 1 ))
then
	echo -n "Mediāna ir "
	echo "scale=1;(${sort[$n/2]} + ${sort[$n/2-1]})/2" |bc
else
	echo -n "Mediāna ir "
	echo "${sort[($n-1)/2]}" | bc
fi

t=0
a1=${sort[$t]}
a2=1
b1=$a1
b2=$a2

while (( $t < $n ))
do
	t=`expr $t + 1`
	if [[ "$a1" == "${sort[t]}" ]]
	then
		a2=`expr $a2 + 1`
	else
		a1=${sort[$t]}
		a2=1
	fi

	if (( $a2 > $b2))
	then
		b1=$a1
		b2=$a2
	fi
done

if (( $b2 == 1 ))
then
	echo "Visi skaitli atkartojas vienu reizi"
else
	echo "Moda:" $b1
fi
