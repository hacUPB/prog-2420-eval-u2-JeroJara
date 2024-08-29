# Menu para elegir las 5 operacioes aritmeticas basicas: + - * / %
print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nT. Residuo")
opcion = input("ingrese la opción deseada: ")
opcion = opcion.upper()

if opcion not in ["S","R","M","D","T"]:
    print("OPCIÓN NO VÁLIDA")
else:

    numero1 = float(input("Ingrese el primer valor; "))
    numero2 = float(input("Ingrese el segundo valor: "))

    if opcion == "S" :
        resultado = numero1 + numero2
    # si no, si opcion es R
    elif opcion == "R":
        resultado = numero1 - numero2
    elif opcion == "M" :
        resultado = numero1*numero2
    elif opcion == "D" :
        resultado = numero1/numero2
    elif opcion == "T":
        resultado = numero1%numero2

    print(f"El resultado es: {resultado}")
    
