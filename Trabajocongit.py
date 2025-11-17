print("Calculadora con validación")

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Error: ingresa un número válido.")

def pedir_operador():
    operadores = ["+", "-", "*", "/"]
    while True:
        op = input("Ingresa el operador (+, -, *, /): ")
        if op in operadores:
            return op
        print(" Error: operador no válido.")

num1 = pedir_numero("Ingresa el primer número: ")
operador = pedir_operador()
num2 = pedir_numero("Ingresa el segundo número: ")

if operador == "/" and num2 == 0:
    print(" Error: no puedes dividir para 0.")
else:
    if operador == "+":
        print("Resultado:", num1 + num2)
    elif operador == "-":
        print("Resultado:", num1 - num2)
    elif operador == "*":
        print("Resultado:", num1 * num2)
    elif operador == "/":
        print("Resultado:", num1 / num2)
