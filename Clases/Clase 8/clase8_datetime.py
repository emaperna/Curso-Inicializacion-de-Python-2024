import datetime 

fecha_actual = datetime.date.today()
print(f"La fecha actual es: {fecha_actual}")

fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
print(f"la fecha actual: {fecha_formateada}")
dia = fecha_actual [0:2]
print(f"El dia es: {dia}")

dia_formateado = fecha_actual.strftime("%d")
print(f"El dia formateado: {dia_formateado}")

hora_actual = datetime.datetime.now()
print(f"La hora actual sin formato: {hora_actual}")
hora_formateada = hora_actual.strftime("%H:%M:")
print(f"La hora actual formateada: {hora_formateada}")