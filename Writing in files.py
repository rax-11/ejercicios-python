

employee_file = open("Employees", "a") # si utilizo "w" en lugar de "a", lo que añada va a sobreescribir todo el archivo
                                        # si cambio Employees a Employees1, se creará un archivo .txt nuevo
employee_file.write("\nAngela - Accountant") # Se añade permanentemente el elemento al archivo externo.txt
employee_file.write("\nKelly - Customer service") # \n añade un espacio y mueve a la siguiente fila
employee_file.close()

