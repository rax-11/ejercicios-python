monthConversions = {
    "Jan": "January",
    "Feb": "Febrero",
    "Mar": "Marzo",
    "Abr": "Abril",
    "May": "Mayo",
    "Jun": "Junio",
    "Jul": "Julio",
    8: "Agosto",
    9: "Septiembre",
    "Oct": "Octubre",
    "Nov": "Noviembre",
    "Dic": "Diciembre"
}
mes = input("Introduce un mes: ")
print(monthConversions.get( mes , "No es una key válida"))

# Diccionarios se ponen entre {}, clave = valor, cada clave debe ser única
# tambien se puede usar print(monthConversions["Dic"])
# Las keys no siempre deben ser strings, también pueden ser números
