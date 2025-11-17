print("******Calculadora******")
print("* Selecciona una operación *")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input(" Ingresa el número de la opción: ")

if opcion not in ("1", "2", "3", "4"):
    print("Opción no válida.")
else:
    try:
        num1 = float(input(" Ingresa el primer número: "))
        num2 = float(input(" Ingresa el segundo número: "))
        
        resultado = None
        
        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado de la suma: {resultado}")
    
        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado de la resta: {resultado}")
    
        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado de la multiplicación: {resultado}")
    
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado de la división: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    
    except ValueError:
        print(" Error: Ingresa solo valores numéricos válidos.")