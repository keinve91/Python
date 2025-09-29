# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
numero=int(input("Introduce un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
edad=int(input("Ingrese su edad: "))
if edad>=18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
texto=input("Introduce un texto: ")
if not texto:
    print("Esta vacio")
else:
    print("No esta vacio")
# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))
if(numero1>numero2):
    print(f"El numero {numero1} es mayor que el numero {numero2}")
elif(numero1<numero2):
    print(f"El numero {numero1} es menor que el numero {numero2}")
else:
    print("Son numeros iguales")
# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
numero=int(input("Ingrese un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"El numero es divisible por 5 y 3")
else:
    print(f"El numeor no es divisible por 5 y 3")
# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
numero=int(input("Ingrese un numero: "))
if numero%2==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
edad=int(input("Ingrese su edad: "))
if edad >= 18:
    print("Podes votar")
elif edad >= 16:
    print("Podes votar pero con permiso")
else:
    print("No podes votar")
# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
contra="python"
contra2=int(input("Ingrese una contraseña: "))
if(contra == contra2):
    print("La contrasenia es correcta")
else: 
    print("La contrasenia no es correcta")
# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
numero=int(input("Ingrese un numero: "))
if 10 <=numero <=20:
    print(f"el numero {numero} esta entre 10 y 20")
else:
    print(f"el numero {numero} no esta entre 10 y 20")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color = input("Introduce un color (rojo, amarillo, verde): ").lower()
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaucion")
elif color == "verde":
    print("Avanza")
else:
    print("Color no valido")