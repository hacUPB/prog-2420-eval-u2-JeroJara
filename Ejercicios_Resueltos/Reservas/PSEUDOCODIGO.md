```
Inicio

Imprimir "¿Cómo desea que nos dirijamos a usted? ¿Señor o Señora?: "
Leer invocativo
print "Por favor, ingrese su nombre: "
Leer name
print "Por favor, ingrese su apellido: "
Leer lastname
print "¡Gracias por elegirnos! Bienvenido a la mejor Aerolínea del barrio,"invocativo, name, lastname

print "ahora, elija una ciudad de origen: Medellín, Bogotá o  Cartagena : "
Leer origen
print "Y ahora su ciudad de destino : Medellín, Bogotá o Cartagena (recuerde que la ciudad de origen no puede ser igual al destino):"
Leer destino

si origen = destino entonces
    print "No se puede hacer."
fin si

print "¿Qué día de la semana preferiría viajar?: (lunes, martes, miercoles, jueves, viernes, sabado, domingo): "
Leer díasemana
Imprimir "¿Qué día del mes quisiera viajar?: "
Leer diames
si (origen = "Medellín" and destino = "Bogotá") or (destino = "Bogotá" and origen = "Medellín") entonces
 distance = 240
 else
    si (origen = "Medellín" and destino ="Cartagena")or (origen ="Cartagena" and destino = "Medellín")entonces
        distance = 461
        else
            si (origen = "Bogotá" and destino= "Cartagena")or (origen ="Cartagena" and destino = "Bogotá") entonces
                distance = 657
             fin si
        
    fin si
fin si


Si (distance < 400) and (diasemana = "lunes" ó diasemana = "martes"  diasemana = "miercoles" ó diasemana= "jueves") entonces
        precio = 79900
si no
        si (distance <400) and (diasemana = "viernes" o diasemana="sabado" o diasemana= "domingo") entonces
            precio = 119900
        si no
             si  (distance >= 400) and (diasemana = "viernes" o diasemana="sabado" o diasemana= "domingo") entonces 
             precio = 213000
            si no
                    si  (distance >=400) and (diasemana = "lunes" ó diasemana = "martes"  diasemana = "miercoles" ó diasemana= "jueves") entonces
                        precio = 156900
                    fin si
            fin si 
        fin si
fin si

print "¿Dónde prefiere sentarse?: (ventana, pasillo, no me importa dónde): "
Leer preferencia
Si preferencia = ventana entonces
   asiento  = "A"
Si no
    Si preferenica = pasillo
        asiento = "C"
    Si no
        asiento = "B"
    fin si
fin si

numero = generarenteroaleatorio(1,29)

print ("Estimado" ,invocativo, name, lastname "confirmamos su vuelo: volará el día" diasemana, diames "del mes.Desde" ,origen "hasta ", destino "Debes pagar  $ " , precio " Tu asiento es el" ,preferencia, numero " FELIZ VIAJE" )

FIN
```
