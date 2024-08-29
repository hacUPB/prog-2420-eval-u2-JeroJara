

### ### Problema 6 (obligatorio): Calcular la edad de una persona a partir de su fecha de nacimiento y la fecha actual

### **Descripción del Problema:**
### Se desea saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento. Además, le gustaría saber si ya ha cumplido años este año o aún no, y si hoy es su cumpleaños para celebrarlo. Cada una de las fechas está conformada por 3 variables: día, mes y año
 
 ```
 Inicio
 leer dia_naci, mes_naci, año_naci, mes_actu, año_actu, dia_actu

// Primero se calculan los años:
   años = año_actu - año_naci
// ahora se mira si ya se han cumplido esos años, es decir, si el mes_naci y día_naci ya han pasado:
      Si (mes_actu<mes_naci) o
         (mes_actu == mes_naci Y dia_actu < dia_naci) Entonces
         años == años - 1
         imprimir "No has cumplido años."
// Esta parte no la entendí: Cómo hago para hacer los 2 procesos en paralelo
//lUego se calculan los meses:
Si (mes_actu >= mes_naci) entoces
     meses = mes_actu - mes_naci
 FinSi

//Calcular días
si (dia_actu > dia_naci) entonces
   dias = dia_actual - dia_naci
Finsi

si (dia_actu = dia_naci) Y (mes_actu = mes_naci) Y (año_actu = año_actual) entonces
   imprimir "Feliz cumple"
sino
  imprimir "hoy no cumples"
Fin si



      
 Fin
 ```


 ### Problema 1: Determinar el promedio de calificaciones de un estudiante y si ha aprobado o no

Ana quiere saber si ha aprobado sus exámenes finales. Tiene una lista de sus calificaciones y necesita calcular el promedio. Para aprobar, debe tener un promedio de al menos 3.0.

```
Inicio
    leer lista_calificaciones
    leer numero_calificaciones
    definir contador= numero_calificaciones
    mientras contador > 0 entonces:
        definir suma = 0
        leer calificacion
        suma = suma + calificacion
        contador = contador - 1
        
    fin mientras
    dividir suma entre numero_calificaciones = promedio 
    imprimir promedio
    si promedio >= 3 entonces:
        imprimir  "APROBASTE c:"
    fin si

    si promedio < 3 entonces:
       imprimir  "NO APROBASTE :c"
    fin si

Fin
```
### Problema 4: Determinar la distancia total recorrida por un vehículo con registros de velocidad y tiempo

#### María tiene un registro de las velocidades a las que ha conducido su vehículo y el tiempo que ha mantenido cada velocidad. Quiere calcular la distancia total recorrida.
```
Inicio

    Leer lista_velocidades
    Leer lista_tiempos

    Definir distancia_total = 0

    Para i desde 0 hasta cantidad(lista_velocidades) - 1 hacer
        velocidad_actual = lista_velocidades
        tiempo_actual = lista_tiempos
        
        Multiplicar velocidad_actiual por tiempo_actual para obtener distancia
        
        sumar distancia_total a distancia e igualar a distancia_total

    Imprimir distancia_total

Fin
```





inicio 
 leer horas
  si numh > 10 entonces
   costo = 2 *numh
    si no 
      si numh <= 2 entonces
        costo = numh * 5
          si no 
             si  numh<=5 entonces 
               costo = 10 + (numh - 2)*4 
                 si numh<=10 entonces
                   costo = 22 + (numh - 5) * 3
                 FinSi
             FinSi
        FinSi
     FinSi
            imprimir "Debes cobrar", costo
 Fin


 ### TAREA: PSEUDOCODIGO QUE CALCULA EL VALOR DE LA CUOTA 
```
      Inicio
        leer valorcompra
        leer numcuotas
        definir interes= 0.15
        cuotabase= valorcompra/numcuotas
        cuotainicial = cuotabase + (valorcompra * interes)
        imprimir cuotainicial
        mientras valorcompra > 0
        valorcompra= valorcompra - cuotabase
        cuotapagar = (valorcompra*interes) + (cuotabase*

        ValorPagar = valorcompra/numcuotas
         sino 
            mientras cuota > 1 entonces
            definir ValorPagar = 0
            ValorPagar = ValorPagar + valorcompra

      
      Fin
```

```
      Inicio
        leer valorcompra
        leer numcuotas
        leer cuotaAcalcular
        definir interes= 0.15
 /// la primera cuota no tiene intereses ///
        si cuota = 1 entonces
        ValorPagar = valorcompra/numcuotas
 /// Se usa formula del interes compuesto ///
         sino 
            ValorPagar = (valorcompra *(1 + interes)  ^cuotaAcalcular)/numcuotas
        Finsi

        imprimir "el valor de la cuota número", cuotaAcalcular, "es de ", ValorPagar

      Fin
```


