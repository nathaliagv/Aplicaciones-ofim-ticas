print("Calculadora simple")

num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    print("Resultado:", num1 / num2)
else:
    print("Operador no válido")
