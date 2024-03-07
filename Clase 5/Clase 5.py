# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:55:37 2024

@author: Estudiante
"""
#Conjuntos.

conjunto= set()
conjunto={8,20,3,4,5,'Pepe','Maria','Carlos','Juan'}
print(conjunto)

#Agregar elementos.
conjunto.add(85)
print(conjunto)
conjunto.add('Angela')
print(conjunto)

#Buscar elementos
    #Buscar si existe
print('Pepe' in conjunto)
print(21 in conjunto)

    #Buscar si no existe
print(20 not in conjunto)
print(99 not in conjunto)

#Eliminar elementos
conjunto.discard('Pepe')
print(conjunto)
conjunto.discard(3)
print(conjunto)

#Borrar todo
conjunto.clear()
print(conjunto)

#Operciones con conjuntos
con1= {1,2,3,4,5,6,7,8,9,0}
con2={11,12,20,30,40,50,60,89,74}
con3= {1,2,3,4,5,6,7,8,9,0}
con4={'Maria', 50, 'Jose', 4,5,'tinto',7,8,'agua',0}
    #Comparar elementos
print(con1 == con2)
print(con1 != con2)
print(con1 == con3)

    #Tamaños
print(len(con1))
print(len(con2))
print(len(con3))

    #Unir conjuntos
unionc= con1 | con2 | con3
print(unionc)

#Interseccion entre conjuntos
interc= con1 & con2
print(interc)    
interc2= con1 & con3
print(interc2)
interc3= con1 & con4
print(interc3)

#Diferencia entre conjuntos.
diferenciac= con1-con2
print(diferenciac)
diferenciac2=con1-con3
print(diferenciac2)
diferenciac3=con1-con4
print(diferenciac3)
diferenciac4=con4-con1
print(diferenciac4)

#Diferencia simetrica.
simetricac= con1 ^ con2
print(simetricac)

#Definir subconjuntos
c1={1,2,3,4}
c2={4,5,6,7,8,9}
c3={1,2,3,4,5,6,7,8,9,10}
c4={'pepe','maria','juan','camila'}
c5={'pepe','maria','juan','camila','Andrea','Johanna','Andres'}

    #Determinar si c1 es subconjunto de c3
print(c1.issubset(c3))
print(c1.issubset(c2))
print(c2.issubset(c3))
print(c4.issubset(c5))
print(c5.issubset(c4))
print(c4.issubset(c2))