# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20
suma = 15 + 25
print("Suma (15 + 25):", suma)
resta = 50 - 22
print("Resta (50 - 22):", resta)
multiplicacion = 8 * 7
print("Multiplicación (8 * 7):", multiplicacion)
division = 100 / 20
print("División (100 / 20):", division)
# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
remainder = 37 % 5
print("Resto de 37 / 5:", remainder)
# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
numero = 7
minumerofavorito = str(numero) + " es mi número favorito"
print(minumerofavorito)
# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.
repetir = "Python" * 10
print(repetir)
# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
resultado = a > b
print(f"¿{a} > {b}?: {resultado}")
# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.
str1 = "apple"
str2 = "banana"
is_greater = str1 > str2
is_less = str1 < str2
print(f"¿'{str1}' > '{str2}'?: {is_greater}")
print(f"¿'{str1}' < '{str2}'?: {is_less}")
# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.
logica = (10 > 5) and (10 < 20)
print("¿10 > 5 y 10 < 20?:", logica)
# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
logica_or = (7 < 3) or (7 > 5)
print("¿7 < 3 o 7 > 5?:", logica_or)
# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
comparacion_original = 15 > 20
resultado_not = not comparacion_original
print("Resultado de (15 > 20) sin 'not':", comparacion_original) # False
print("Resultado de not (15 > 20):", resultado_not)
# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado
resultado_aritmetico = 10//3
print(f"Resultado aritmético: {resultado_aritmetico}")
combinado = (resultado_aritmetico > 10) and (resultado_aritmetico < 20)
print("¿El resultado aritmético es > 10 y < 20?:", combinado)

