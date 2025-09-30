# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
def dividir_numeros(a, b):
    try:
        result = a / b
        print(f"El resultado es {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar cualquier error en la conversiÃ³n.
def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        print("Error: No se puede transformar a entero.")
# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def leer_contenido_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")
# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def operaciones_con_finally(num1, num2):
    try:
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"MultiplicaciÃ³n: {num1 * num2}")
        print(f"DivisiÃ³n: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Operaciones realizadas correctamente.")
    finally:
        print("Fin de las operaciones.")
# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def obtener_edad_positiva():
    try:
        age = int(input("Introduce tu edad: "))
        if age <= 0:
            raise ValueError("La edad debe ser un entero positivo.")
        return age
    except ValueError as e:
        print(f"Error: {e}")

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.
def acceder_elemento_lista(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print("Error: Ãndice fuera de rango.")
# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def manejar_multiples_excepciones(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Valor invÃ¡lido.")
    except TypeError:
        print("Error: Tipo no compatible.")
# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
class InsufficientFundsError(Exception):
    pass
def simular_transaccion(saldo, monto_retiro):
    try:
        if monto_retiro > saldo:
            raise InsufficientFundsError(
                "Saldo insuficiente para la transacciÃ³n.")
        saldo -= monto_retiro
        print(f"TransacciÃ³n realizada correctamente. Nuevo saldo: {saldo}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def convertir_lista_a_enteros(lista_cadenas):
    integers = []
    for string in lista_cadenas:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se puede transformar en un entero.")
    return integers
# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
def calcular_raiz_cuadrada(numero):
    try:
        if numero < 0:
            raise ValueError(
                "No se puede calcular la raÃ­z cuadrada de un nÃºmero negativo.")
        return numero ** 0.5
    except ValueError as e:
        print(f"Error: {e}")