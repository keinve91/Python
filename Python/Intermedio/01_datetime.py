from datetime import datetime,time,date,timedelta
# 1. Crea una variable con la fecha y hora actual.
ahora=datetime.now()
print(ahora)
# 2. Imprime solo el año, mes y día de la fecha actual.
print(f"{ahora.year}-{ahora.month}-{ahora.day}")
# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.
navidad=datetime(2025,12,25)
print(navidad)
# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hora=time(16,20,20)
print(hora)
# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
hoy=date.today()
añonuevo=date(hoy.year+1,1,1)
diferencia=añonuevo-hoy
print(f"Faltan {diferencia.days} dias.")
# 6. Crea una función que reciba una fecha y devuelva su timestamp.
def ver_timestamp(date):
    return date.timestamp()
print(ver_timestamp(ahora))
# 7. Suma 30 días a la fecha actual usando timedelta.
futuro=ahora+timedelta(days=30)
print(futuro)
# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).
fecha=datetime(2018,12,9)
nuevafecha=fecha+timedelta(days=35)
print(nuevafecha)
# 9. Compara dos fechas y muestra cuál es anterior.
fecha2=datetime(2018,12,8)
if fecha > fecha2:
    print(f"la fecha '{fecha2}' es anterior que esta fecha '{fecha}'")
else:
    print(f"la fecha '{fecha}' es anterior que esta fecha '{fecha2}'")
# 10. Crea una lista con varias fechas y ordénalas cronológicamente.
lista_fechas = [
    datetime(2023, 12, 15, 10, 0, 0),
    datetime(2024, 1, 1, 0, 0, 0),
    datetime(2023, 12, 15, 9, 30, 0),
    datetime(2024, 1, 3, 18, 0, 0),
    datetime(2023, 5, 20, 12, 0, 0)
]
ordenarfechas=sorted(lista_fechas)
for f in ordenarfechas:
    print(f)