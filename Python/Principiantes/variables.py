# 1. Declara y asigna valores a las siguientes variables:
# â€¢    name: una cadena que contenga tu nombre.
# â€¢    age: un nÃºmero entero que represente tu edad.
# â€¢    height: un nÃºmero flotante que represente tu altura.
# â€¢    Imprime cada variable en una lÃ­nea separada.
name="Kevin"
age=19
height=1.75
print(name)
print(age)
print(height)
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
año_str = str(age)
print("Tengo " + año_str + " años.")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
estudiante = True # O False, según corresponda
print("¿Es estudiante?:", estudiante)
# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
completo="Kevin Brian Joel"
print("Mi nombre tiene", len(completo), "caracteres")
# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad = "Kevin", "Cruz", "Buenos Aires"
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Ciudad:", ciudad)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color = input("Ingresa tu color favorito: ")

print("Tu color favorito es:", color)
# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruta = "Manzana"
print("Fruta inicial:", fruta)

fruta = "Naranja"
print("Fruta reasignada:", fruta)
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
precio = 9.99
print("Precio decimal:", precio)

precio_int = int(precio)
print("Precio entero:", precio_int)
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address = "Avenida siempreviva"
address_len = len(address)
print(f"La longitud de la dirección '{address}' es: {address_len} caracteres.")

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone = int(333324418)

print(f"First: {phone}")

phone = 3019733333

print(f"Second: {phone}")

print(type(phone))