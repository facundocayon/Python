#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
solicitar el valor en fahrenheit y capturarlo
mientras no se ingrese un valor correcto:
	informar que se debe ingresar un valor
	volver a solicitar el valor en fahrenheit y capturarlo
realizar la conversion e informar el valor en centigrados por pantalla
"""
print("""
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ 
||F |||A |||H |||R |||E |||N |||H |||E |||I |||T |||       |||T |||O ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|
 ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||C |||E |||L |||S |||I |||U |||S |||       |||C |||O |||N |||V |||E |||R |||T |||E |||R ||
||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ 
||T |||O |||O |||L ||
||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|

""")
def ingreso_valido(ingreso):
	if ingreso.startswith("-"):
		if ingreso[1:].isnumeric() and int(ingreso) > -1000:
			return True
		else:
			return False
	elif ingreso.isnumeric():
		return True
	else:
		return False

print ("")
print (" Presione Enter para comenzar:")
input()
fahrenheit = input(" Ingrese grados fahrenheit = ")

while not ingreso_valido(fahrenheit):
	print ("")
	print(" Ups! Ha ingresado un valor incorrecto.")
	print ("")
	fahrenheit = input(" Ingrese grados fahrenheit = ")
celsius = (int(fahrenheit) - 32) * 5/9
print("")
print(" Son centigrados = " + str(celsius))
