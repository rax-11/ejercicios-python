

employee_file = open("Employees", "r")
# r = only read
# w = writing or editing the information
# a = you can only add information
# r+ = reading and writing

# print(employee_file.readable()) # dependiendo si el file puede ser leido va a salir tru o false
# print(employee_file.read()) # muestra la información dentro del file
# print(employee_file.readline()) # lee solo la primera linea del file
# print(employee_file.readline()) # lee la segunda linea del archivo y asi sucesivamente
# print(employee_file.readlines()) # POne todas las lineas del archivo en una lista

for employee in employee_file.readlines():
    print(employee)
employee_file.close()
