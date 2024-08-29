# EJERCICIO DE IMPRESION DE DATOS

print("University wow")
print("uno","dos", "tres")
print('...y ella me dijo "quiero que te vayas"')
print("...y ella me dijo:\"quiero que te vayas\"" )
print ("1.Imprimir\n2.\n")
#si quiero que me imprima el \, debo poner otro \ al lado.
print('%'*40)

#imc = peso/altura^2

peso = int(input("ingrese su peso en kg: "))
altura = float(input ("ingrese su altura en metros"))
IMC = peso/(altura*altura)
print("Su IMC es: ", IMC)
