num1 = float(input("Pon el primer numero: "))
# float convierte el input, que normalmente convierte en string, en un número
op = input("Pon el operador: ")
num2 = float(input("Pon el segundo numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")