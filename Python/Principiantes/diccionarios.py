# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
diccionario={"nombre":"Kevin", "anio":"19","pais":"Argentina"}
print(diccionario)
# 2. Accede al valor de la clave name en el diccionario.
print(diccionario["nombre"])
# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
diccionario["trabajo"]="Programador"
print(diccionario)
# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
diccionario["anio"]=20
print(diccionario)
# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del diccionario["pais"]
print(diccionario)
# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
alcuadrado={x:x**2 for x in range(1,6)}
print(alcuadrado)
# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
print("anio" in diccionario)
# 8. Imprime solo las claves del diccionario.
print(diccionario.keys())
# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(diccionario.keys()))
# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
llaves=["name","age","job"]
nuevodiccionario=diccionario.fromkeys(llaves, "Desconocido")
print(nuevodiccionario)

print(diccionario.items())