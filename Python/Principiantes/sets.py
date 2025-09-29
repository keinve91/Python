# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.
miset={1,2,3,4,5}
print(miset)
# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
miset={1,2,3,4,5}
miset.add(6)
print(miset)
# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?
miset={1,2,3,4,5}
miset.add(5)
print(miset)
# No permite duplicados
# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in miset)
# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
miset.remove(4)
print(miset)
# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
miset.clear()
print(miset)
# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.
miset={"manzana","naranja","platano"}
lista=list(miset)
print(lista[0])
# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
miset1={1,2,3}
miset2={4,5,6}
union=miset1.union(miset2)
print(union)
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
miset1={1,2,3,4}
miset2={3,4,5,6}
diferencia=miset1.difference(miset2)
print(diferencia)
# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
miset={1,2,3}
del miset
#print(miset) sale un error