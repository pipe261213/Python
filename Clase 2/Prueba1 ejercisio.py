# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:08:17 2024

@author: Estudiante
"""

#Crear un programa que pida 4 notas y las almacen en una lista
#Debe calcular la definitiva y debe mostrar el resultado

n1=int (input("Su primera nota es: "))

n2=int (input("Su segunda nota es: "))

n3=int (input("Su tercera nota es: "))

n4=int (input("Su cuarta nota es: "))

lista=[n1,n2,n3,n4]

print(f"Sus notas fueron: {lista}")

suma=(n1+n2+n3+n4)
definitiva=(suma/4)
print(f"Su definitiva es {definitiva}")

