# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:25:08 2024

@author: Estudiante
"""
#Realizado por Johan Muñoz

#Creación de conjuntos
conjunto1=set()
conjunto2=set()
conjunto1={'Juan','Pedro','Marta',1,2,3,4,5}
conjunto2={'Catalina','Laura','Lucia',6,7,8,9,0}
print(conjunto1)
print(conjunto2)

#Buscar
    #Si existen.
        #Conjunto1
print('Juan' in conjunto1)
print('Laura' in conjunto1)
print(1 in conjunto1)
print(7 in conjunto1)
        #Conjunto2
print('Laura' in conjunto2)
print('Pedro' in conjunto2)
print(9 in conjunto2)
print(5 in conjunto2)

    #Si no existen
        #Conjunto1
print('Laura' not in conjunto1)
print('Juan' not in conjunto1)
print(7 not in conjunto1)
print(1 not in conjunto1)
        #Conjunto2
print('Pedro' not in conjunto2)
print('Laura' not in conjunto2)
print(5 not in conjunto2)
print(9 not in conjunto2)

#Creación conjuntos Materias y notas.
conjunto3materias={'Ingenieria de materiales','Python','Arquitectura grecolatina'}
conjunto4notas={4,5,2}
print(conjunto3materias)
print(conjunto4notas)

#Agregar elementos
conjunto3materias.add('Cartografía')
conjunto4notas.add(3)
print(conjunto3materias)
print(conjunto4notas)

#Determinar si son subconjuntos.
    #conjunto1 subconjunto del conjunto2
print(conjunto1.issubset(conjunto2))
print(conjunto4notas.issubset(conjunto3materias))

#Realizado por Johan Muñoz