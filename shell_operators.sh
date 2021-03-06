#!/bin/bash







# 4.piemērs operacijas ar argumentiem
if [ $# == 2 ]
# ja (if) skriptam nodotu argumentu skaits ($#) ir vienāds (==) ar$
then
# tad tiekmizpildītas visas sekojosas darbības līdz ... 
a=$1
b=$2
val41=`expr $a + $b`
echo "$a + $b + "$val41
val42=`expr $a - $b`
echo "$a - $b + "$val42
val43=`expr $a \* $b`
echo "$a * $b + "$val43
val44=`expr $a / $b`
echo "$a / $b + "$val44
val45=`expr $a % $b`
echo "$a % $b + "$val45
#  ... šai vietai
fi




# 3.piemērs operacijas r mainīgajiem
: <<'END'
a=56
b=32
val31=`expr $a + $b`
echo "$a + $b + "$val31
val32=`expr $a - $b`
echo "$a - $b + "$val32
val33=`expr $a \* $b`
echo "$a * $b + "$val33
val34=`expr $a / $b`
echo "$a / $b + "$val34
val35=`expr $a % $b`
echo "$a % $b + "$val35
END

 
# 2. piemers - opreacijas ar konstantēm
: <<'END'
val21=`expr 2 + 3`
echo "2 + 3 + "$val21
val22=`expr 2 - 3` 
echo "2 - 3 + "$val22
val23=`expr 2 \* 3` 
echo "2 * 3 + "$val23
val24=`expr 2 / 3` 
echo "2 / 3 + "$val24
val25=`expr 2 % 3` 
echo "2 % 3 + "$val25



# 1.piemērs - izteiksmes pieraksts
: <<'END' #komentara bloka sakums
val11="expr 2+2"
echo "2 + 2 rezultāts (pēdiņas, nav atstarpes) "$val11
val12="expr 2 + 2"
echo "2 + 2 rezultāts (pēdiņas, nav atstarpes) "$val12
val13='expr 2+2'
echo "2 + 2 rezultāts (parasti apostrofi, nav atstarpes) "$val13
val14='expr 2 + 2'
echo "2 + 2 rezultāts (parasti apostrofi, ir atstarpes) "$val14
val15=`expr 2+2`
echo "2 + 2 rezultāts (neparasti apostrofi, nav atstarpes) "$val15
val16=`expr 2 + 2`
echo "2 + 2 rezultāts (neparasti apostrofi, ir atstarpes) "$val16
END
