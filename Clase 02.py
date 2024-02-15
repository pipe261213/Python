# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:54:25 2024

@author: Estudiante
"""
#Listas
lista=['Carlos', 'Perez','edad',20]
# confirmar tamaño
tam=len(lista)
print(f"El tamaño de la lista es de: {tam}")

#Agregar elementos a la lista
lista.append(2)

tam1=len(lista)
print(f"El tamaño de la lista es de: {tam1}")
print(lista)
lista.append(2)

#Buscar coindidencias
coincidencia=lista.count(2)
print(F"El numero 2 aparece {coincidencia} veces.")

#Mostrar índice
indice=lista.index(2)
print(f"La ubicación del elemento 2 es: {indice}")

#Insertar en un lugar especifico
lista.insert(0, "Colombia")
print(lista)

#Extraer el ultimo elemneto
ultimo=lista.pop(4)
print(ultimo)
print(lista)

#Extraer elemneto especifico
ultimo=lista.pop(3)
print(ultimo)
print(lista)

#Agregar mas de un elemnto a la lista
lista.extend([0,0])
print(lista)

#Borrar primera coincdencia
lista.remove(0)
print(lista)

#Limpiar la lista
lista.clear()
print(lista)

#Invertir la lista
lista2=['Carlos', 'Perez','edad',20]
print(lista2)
lista2.reverse()
print(lista2)

#Ordenar Lista
lista.sort()
print(lista2)

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

