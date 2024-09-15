
def main():
########FUNCIONES################
    from os import system
    from random import randint
    def registro(invocativo:str,nombre:str,apellido:str):
        if invocativo.lower() == "señor" or invocativo.lower() == "señora":
            print("¡Gracias por elegirnos! Bienvenido a la mejor Aerolínea del barrio, ",invocativo, nombre, apellido)
        else:
            print("Género no válido")
    
    
    def asiento(preferencia):
        if preferencia.lower() == "pasillo":
            asiento_pasajero = "C"
        elif preferencia.lower() == "ventana":
            asiento_pasajero = "A"
        else:
            asiento_pasajero = 'B'
        
        numero = randint(1,29)
        return numero,asiento_pasajero
    
    ciudades = ["medellín","bogotá","cartagena"]
    dias_semana = ["lunes","martes","miércoles","jueves"]
    dias_finde = ["viernes","sábado","domingo"]
    
    
    
    def precio(origen):
    
            if origen.lower() in ciudades:
                destino = str(input("Por favor ingrese la ciudad de destino:  "))
                if destino.lower() in ciudades and destino != origen:
                    dia_semana2 = str(input("Por favor ingrese el día de la semana que desea viajar (De lunes a domingo):  "))
                    
                    if dia_semana2.lower() in dias_semana:
                        if (origen.lower() == "bogotá" and destino.lower() == "medellín") or (origen.lower() == "medellín" and destino.lower() == "bogotá"):
                            distance = 240
                            price = 79900
                        
                        elif (origen.lower() == "bogotá" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "bogotá"):
                            distance = 657
                            price = 156900
                        
                        elif (origen.lower() == "medellín" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "medellín"):
                            distance = 461
                            price = 156900
                        else:
                            print("Destino no válido")
                    
    
    
                    elif dia_semana2.lower() in dias_finde:
                        if (origen.lower() == "bogotá" and destino.lower() == "medellín") or (origen.lower() == "medellín" and destino.lower() == "bogotá"):
                            distance = 240
                            price = 119900
                        
                        elif (origen.lower() == "bogotá" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "bogotá"):
                            distance = 657
                            price = 213000
                        
                        elif (origen.lower() == "medellín" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "medellín"):
                            distance = 461
                            price = 213000
    
                        else:
                            print("Destino no válido")
                    
                    else:
                        print("Día de la semana no válido")
                
                else:
                    print("Destino no puede ser igual al origen o ciudad no válida")
            
            return destino,price
    
    def registro(invocativo,nombre,apellido):
        if invocativo.lower() == "señor" or invocativo.lower() == "señora":
            return print("¡Gracias por elegirnos! Bienvenido a la mejor Aerolínea del barrio, ",invocativo, nombre, apellido)
        else:
            print("Género no válido")
    
    #########################################CÓDIGO PRINCIPAL###########################################
    
    
    invocativo = str(input("¿Cómo desea que nos dirijamos a usted? ¿Señor o Señora?:  "))
    nombre = str(input(("Por favor, ingrese su nombre: ")))
    apellido = str(input("Por favor, ingrese su apellido:   "))
    
    system("cls")
    
    registro(invocativo,nombre,apellido)
    
    origen = str(input("Por favor ingrese su ciudad de origen (Medellín, Bogotá o Cartagena ):  "))
    
    llegada,precioboleto = precio(origen)
    
    
    preferencia = str(input("¿Dónde prefiere sentarse? (Pasillo, Ventana, sin preferencia):  "))
    
    asiento(preferencia)
    
    dia_mes = int(input("Por favor escriba el día del mes que desea viajar (1 al 30):  "))
    system("cls")
    mes = str(input("¿Qué mes desea viajar?:  "))
    system("cls")
    
    
    print(f"Tu vuelo de {origen} a {llegada} el día {dia_mes} de {mes.lower()} está reservado.\n El precio de su tiquete es ${precioboleto} \n Asiento: {asiento(preferencia)} ")
    


if __name__ == "__main__":
    main()
