#!/bin/bash
#zad1
string="Hello world"
echo $string

#zad2
ls /dev -R | wc -l

#zad4 - zamek

code="kod"
read user_code

if [[ $code == *"$user_code"* ]]
then
 echo poprawny kod!
else
 echo niepoprawny kod!
fi

#zad5
echo "Podaj imie, nazwisko i rok urodzenia (oddzielajac spacja)"
read imie nazwisko rok

echo Twoje imie to: $imie
echo Twoje nazwisko to: $nazwisko
echo Twoj rok urodzenia to: $rok

#kalkulator
while true; do
    read -p "what's the first number? " n1
    read -p "what's the second number? " n2
    PS3="what's the operation? "
    select ans in add subtract multiply divide quit; do
        case $ans in 
            add) op='+' ; break ;;
            subtract) op='-' ; break ;;
            multiply) op='*' ; break ;;
            divide) op='/' ; break ;;
	    quit) exit 0 ;;
            *) echo "invalid response" ;;
        esac
    done
    ans=$(echo "$n1 $op $n2" | bc -l)
    printf "%s %s %s = %s\n\n" "$n1" "$op" "$n2" "$ans"
done


#zad6 drzewo rekurencyjne

function przejdz() {
for plik in "$1"/*
do
    if [ ! -d "${plik}" ] ; then
        echo "${plik}"
    else
        echo "rekurencja na: ${plik}"
        przejdz "${plik}"
    fi
done
}

function main() {
    przejdz "$1"
}

main "$1"
