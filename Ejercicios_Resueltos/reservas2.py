
from modulo import registro
from os import system
from modulo import asiento
from modulo import precio
import datetime

invocativo = str(input("¿Cómo desea que nos dirijamos a usted? ¿Señor o Señora?:  "))
nombre = str(input(("Por favor, ingrese su nombre: ")))
apellido = str(input("Por favor, ingrese su apellido:   "))
registro(invocativo,nombre,apellido)


ciudades = ["medellín","bogotá","cartagena"]
dias_semana = ["lunes","martes","miércoles","jueves"]
dias_finde = ["viernes","sábado","domingo"]

origen = str(input("Por favor ingrese su ciudad de origen (Medellín, Bogotá o Cartagena ):  "))

llegada,precioboleto = precio(origen)


preferencia = str(input("¿Dónde prefiere sentarse? (Pasillo, Ventana, sin preferencia):  "))

asiento(preferencia)

dia_mes = int(input("Por favor escriba el día del mes que desea viajar (1 al 30):  "))
mes = str(input("¿Qué mes desea viajar?:  "))

print(f"Tu vuelo de {origen} a {llegada} el día {dia_mes} de {mes.lower()} está reservado.\n El precio de su tiquete es ${precioboleto} \n Asiento: {asiento(preferencia)} ")

