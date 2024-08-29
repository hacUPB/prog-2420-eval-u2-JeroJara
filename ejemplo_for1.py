aviones = ["A320", "787", "Antonov124", "Espiritu San Luis"]
cont = 1
for avion in aviones: 
    print(f"Avión {cont} -->{avion}")
    cont = cont + 1

# el mismo bucle con while:

indice = 0
cont = len(aviones) #len(aviones) calcula el numero de elementos en lista
while indice < cont:
    print(f"Avión {indice +1} -->{aviones[indice]}") 
    # indice = indice + 1
    indice += 1 

for i in range(5):
    print(f"Avion {i+1} --> {aviones[i]}")
for i in range(100):
    print ("HI")
# pedir al usuario qu eingrese una frase y contar cuantas "a" tiene
frase = input("Ingrese una frase: ")
contador = 0
for letra in frase:
    if letra == "a":
        contador += 1
    