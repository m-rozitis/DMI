#!/bin/bash
#if () then ... elif ()then ... else ... fi
echo "Ievadi pirmo skaitli"
read a
echo "Ievadi otro skaitli"
read b
echo "Ievadi trešo skaitli"
read c
a=$1
b=$2
c=$3
echo "$a $b $c"
echo "$a $c $b"
echo "$b $a $c"
echo "$b $c $a"
echo "$c $a $b"
echo "$c $b $a"



: <<'END'
a=$1
if (( $a > 0 ))
then
   echo "Izdr. no galv. zara - jā gad.  $a > 0"
elif (( $a == 0 ))
then
   echo "Izdr. no alt. zara - jā gad. $a == 0"
else
   echo "Izdr. no alt. zara - nē gad. $a > 0"
fi



: <<'END'
#if () then  ... else .. fi
a=$1
if (( $a > 0 ))
then
   echo "Izdr. no galv. zara - jā gad.  $a > 0"
else
   echo "Izdr. no galv. zara - nē gad. $a > 0"
fi
END


: <<'END'
#if () then ... fi
a=$1
if (( $a > 0 ))
then
   echo "Izdruka no galvenā zara (jā gadījums) - $a > 0"
fi
END
