
def main():
   from os import system

alt_inicial= float(input("Especifique la altitud inical del satélite (en kilómetros): "))


coarrastre= float(input(" Especifique el coeficiente de arrastre del satélite "))


altmin = float(input("Ingrese la altitud mínima de seguridad (en kilómetros): "))

system("cls")

orbitas = 0

altactual = alt_inicial

while altactual > altmin:
    
    altperdida = coarrastre * altactual

    altactual = altactual -altperdida

    coarrastre = coarrastre + 0.0005447

    orbitas +=1

    print (f"En la órbita {orbitas}, la altura fue de {altactual} y el coeficiente de arrastre fue de {coarrastre}")

if altperdida < 0.0034:
    print(f" El cohete logró estabilizarse después de {orbitas} órbitas. \n La última altitud registrada fue de {altactual}km")
else:
    print (f"El cohete reingresó a la atmósfera después de {orbitas} órbitas")
 
if __name__ == "__main__":
    main()
