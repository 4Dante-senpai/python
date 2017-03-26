#!/usr/bin/env python
# -*- coding: utf-8 -*-

frase = raw_input('ingrese la frase')
palabra = raw_input('ingrese la palabra a buscar');
aux = frase.split(' ')

buscar = palabra.lower()

print (aux)
print (buscar) 
cont = 0

for pala in aux:
	pala = pala.lower()
	palabrav = pala.split(buscar)
	print (palabrav)
	if len(palabrav) >= 2:
		cont = cont + 1
		
print (cont)



	
	




