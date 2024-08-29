#trabajador

horas = int(input("Ingrese el número de horas"))
valorhora = int(input("Ingrese el valor de la hora"))
if horas >50 or horas <0:
    print ("No se permite")
    total = 0
elif horas > 45:
    total = valorhora*40 + valorhora *2*5 + valorhora *3*(horas-45)
elif horas > 40:
    total = valorhora*40 + valorhora*2*(horas-40)
else:
    total = valorhora*horas
if horas <= 50:
    print(f"El total a pagar a su trabajdaro es: ${total}")
