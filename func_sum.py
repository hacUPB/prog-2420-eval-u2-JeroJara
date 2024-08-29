Lista = [4,54,66,77,32,11,12,34,34,56,7,5,3,6,77,44,2,2,45,78,978]

acum = 0
numelementos = len(Lista)
cont = 0
while cont < numelementos:
    acum += Lista[cont]
    cont +=1
print (f"la suma es {acum} y debe dar {sum(Lista)}")


