# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
texto = "Aprendiendo Python"
print(len(texto))
# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
print("Hola" + " " + "Mundo")
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
texto = "Primera linea\nOtra linea"
print(texto)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Kevin"
apellido = "Cruz"
anio = 25
print(f"Mi nombre es {nombre} {apellido} y tengo {anio} años.")
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
texto = "Python"
p, y, t, h, o, n = texto
print(p)
print(y)
print(t)
print(h)
print(o)
print(n)
# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
texto = "Programación"
slice_result = texto[3:7]
print(f"Subcadena de '{texto}' [3:7]: {slice_result}")
# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
texto = "Python"
reversa = texto[::-1]
print(f"Cadena invertida de '{texto}': {reversa}")
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
texto = "aprendiendo python"
print(texto.upper())
# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
texto = "Programación en Python"
print(texto.count("n"))
# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
texto = "12345"
print(texto.isnumeric())