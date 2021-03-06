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
	diff <(seq 1 100) <(./ex01/numbers.py)
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
	diff <(echo "Oregon") <(./ex04/state.py Salem)
	diff <(echo "Unknown capital city") <(./ex04/state.py toto)
	diff <(true) <(./ex04/state.py)
	diff <(true) <(./ex04/state.py Salem Denver)
	diff <(true) <(./ex04/state.py Salem Denver Ile-De-France)
}

test_ex05() {
	diff <(echo "Salem is the capital of Oregon (akr: OR)
Montgomery is the capital of Alabama (akr: AL)
Toto is neither a capital city nor a state
Montgomery is the capital of Alabama (akr: AL)") \
		 <(./ex05/all_in.py "Salem , ,Alabama, Toto , ,MontGOmery")
	diff <(echo "Trenton is the capital of New Jersey (akr: NJ)") \
		 <(./ex05/all_in.py " ,nEw jeRsEy, , ")
	diff <(true) <(./ex05/all_in.py)
	diff <(true) <(./ex05/all_in.py Salem Denver)
}

test_ex06() {
	diff <(echo "Johnson
King
Berry
Burton
Garcia
Hendrix
Richards
Beck
Page
Clapton
Allman
Cooder
Santana
Ramone
Thompson
Vaughan
Hammett
Cobain
Frusciante
White") <(./ex06/my_sort.py)
}


for i in {0..6}; do
	echo "+ Testing ex0$i:"
	test_ex0$i
	echo
done
