```
Inicio
print "indique la altitud inicial del satélite en Km"
leer alt1
print "Indique el coeficiente de arrastre (un valor decimal pequeño)"
leer coarr
print "indique la altitud mínima de seguridad en Km"
leer altmin
orbitas = 0
altactual = alt1
mientras altactual > altmin
    altperdida = coarr * altactual
    altactual = altactual - altperdida
    coarr = coarr + 0.00005447
    orbitas = orbitas + 1
    print (f"En la órbita {orbitas}, la altura fue de {altactual} y el coeficiente de arrastre valía {coarr}")
fin mientras


si altperdida < 0.0034 entonces
    print "El cohete se estabilizó después de {orbitas} orbitas. La última altitud registrada fue de {altactual}"
si no
    print "El cohete volvió a la atmósfera después de {orbitas}"
fin si

Fin
