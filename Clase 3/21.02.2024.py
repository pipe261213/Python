# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:38:02 2024

@author: Estudiante
"""

#Operaciones con listas
paises=['Colombia','Argentina','Chile','Paraguay','Ecuador']
print(paises)
datop3=paises[2]
print(datop3)

#Agregar campos
paises.insert(1,'Peru')
print(paises)
paises[4]='Corea del Norte'
print(paises)

#Imprimir desde una pocision especifica
print(paises[2:4])

#Duplicar lista
lista2=['casa','perro','gato']*2
print(lista2)

#Concatenar lista
lista3=['arroz','pan','frijol']
lista4=[1,2,3,4,5]
union=lista3 + lista4
print(union)

#Buscar si un valor existe
print('perro' in lista3)
uniona=lista2 + lista3 + lista4
print('perro' in uniona)

#Tuplas
t1=(1,2,3,'a','b')
print(t1)
t2=list(t1)
print(t2)

l2=tuple(lista4)
print(l2)

#Conjuntos
