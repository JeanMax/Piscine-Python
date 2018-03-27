#!/bin/bash

test_ex00() {
	diff <(echo "42 est de type <class 'int'>
42 est de type <class 'str'>
quarante-deux est de type <class 'str'>
42.0 est de type <class 'float'>
True est de type <class 'bool'>
[42] est de type <class 'list'>
{42: 42} est de type <class 'dict'>
(42,) est de type <class 'tuple'>
set() est de type <class 'set'>") <(./ex00/var.py)
}

test_ex01() {
	diff <(for i in {1..100}; do echo $i; done) <(./ex01/numbers.py)
}

test_ex02() {
	diff <(echo "1942 : Garcia
1946 : Allman
1925 : King
1945 : Clapton
1911 : Johnson
1926 : Berry
1954 : Vaughan
1947 : Santana
1944 : Beck
1943 : Richards
1962 : Hammett
1967 : Cobain
1948 : Ramone
1975 : White
1970 : Frusciante
1949 : Thompson
1939 : Burton") <(./ex02/var_to_dict.py)  # TODO: python hash-tables aren't sorted...
}

test_ex03() {
	diff <(echo "Salem") <(./ex03/capital_city.py Oregon)
	diff <(echo "Unknown state") <(./ex03/capital_city.py toto)
	diff <(true) <(./ex03/capital_city.py)
	diff <(true) <(./ex03/capital_city.py Oregon Alabama)
	diff <(true) <(./ex03/capital_city.py Oregon Alabama Ile-De-France)
}

test_ex04() {
	diff <(echo "Oregon") <(./ex04/erehW.py Salem)
	diff <(echo "Unknown capital city") <(./ex04/erehW.py toto)
	diff <(true) <(./ex04/erehW.py)
	diff <(true) <(./ex04/erehW.py Salem Denver)
	diff <(true) <(./ex04/erehW.py Salem Denver Ile-De-France)
}

test_ex05() {
	diff <(echo "Salem is the capital of Oregon (akr: OR)
Montgomery is the capital of Alabama (akr: AL)
Toto is neither a capital city nor a state
Montgomery is the capital of Alabama (akr: AL)") \
		 <(./ex05/whereto.py "Salem , ,Alabama, Toto , ,MontGOmery")
	diff <(echo "Trenton is the capital of New Jersey (akr: NJ)") \
		 <(./ex05/whereto.py " ,nEw jeRsEy, , ")
	diff <(true) <(./ex05/whereto.py)
	diff <(true) <(./ex05/whereto.py Salem Denver)
}

test_ex06() {
	diff <(echo "Stacy
Jill
Juan
Steve
Dom
Frank") <(./ex06/CoffeeCroissant.py)
}


test_ex00
test_ex01
test_ex02
test_ex03
# test_ex04
# test_ex05
# test_ex06
