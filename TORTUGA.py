#viajes

presup = int(input ("Ingrese su presupuesto: "))
costokm = 100
distancia = presup / costokm
if distancia < 1500:
    print("Esta vez no se pudo")
elif distancia <1600:
    print("Viaja a México")
elif distancia < 2400:
    print("Viaja a P.V")
elif distancia < 3600:
    print("Viaja a Acapulco")
else :
    print("Puedes viajar a Cancún")
    


