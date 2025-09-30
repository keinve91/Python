# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
i=1
while i<=10:
    print(i)
    i+=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
numeros=[10,20,30,40,50]
for numero in numeros:
    print(numero)
# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
i=1
suma=0
while i<=100:
    suma+=i
    i+=1

print(suma)
# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
palabra="Python"
for letra in palabra:
    print(letra)
# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
i=1
while i<=50:
    if i%7 == 0:
        print(i)
        break
    i+=1
# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
persona={"name": "Brais", "age": 37, "country": "Galicia"}
for llave in persona:
    print(llave)
# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
for i in range(3):
    print(i)
# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
lista=[30, 10, 30, 20, 30, 40]
cont=0
for numero in lista:
    if numero==30:
        cont+=1
print(cont)
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = ["Ana", "Luis", "María", "Brais","Carlos"]
for nombre in nombres:
    if nombre=="Brais":
        print("Se encontro Brais")
        break