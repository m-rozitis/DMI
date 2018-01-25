#!/bin/bash
echo "Lietotāj, lūdzu, ievadi skaitļus: "
read input
a=($input)
n=${#a[@]}


sort=($(printf "%s\n" "${a[@]}" | sort -n))
echo "Skaitļi augošā secībā: "${sort[@]}


echo "Lielākais skaitlis ir " ${sort[n-1]}
echo "Mazākais skaitlis ir " ${sort[0]}


summa=0
k=0
while (( $k < $n ))
do
	summa=`expr $summa + ${sort[$k]}`
	k=`expr $k + 1`
done
vsk=`expr $summa / $n`
dsk=`expr $summa % 1$n`
echo "Vidējā vērtība ir " $vsk "." $dsk


if (( n % 2 == 1 ))
then
	echo -n "Mediāna ir "
	echo "${sort[($n-1)/2]}" | bc
else
	echo -n "Mediāna ir "
	echo "scale=2;(${sort[$n/2]} + ${sort[$n/2-1]})/2" |bc
fi


k=0
sk1=${sort[$k]}
n1=1
sk2=$sk1
n2=$n1

while (( $k < $n ))
do
	k=`expr $k + 1`
	if [[ "$sk1" == "${sort[k]}" ]]
	then
		n1=`expr $n1 + 1`
	else
		sk1=${sort[$k]}
		n1=1
	fi

	if (( $n1 > $n2))
	then
		sk2=$sk1
		n2=$n1
	fi
done
echo "Moda:" $sk2
