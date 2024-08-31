#### Para resolver el ejercicio propuesto, podemos enlistar  las variables de entrada de la siguiente manera:
#### altitud inicial: alt1
#### Coeficiente de arrastre: coarr
#### Altitud mínima de seguridad: altmin

#### Y las variables de salida vendrían siendo la última altitud registrada en cada órbita = altactual,  el número de la órbita = orbitas, y el último dato registrado del coeficiente de arrastre en determinada órbita = coarr

#### Además, para saber cuándo se pierde o no suficiente altura para que el satélite reingrese a la atmósfera, se debe añadir una constante para hacer un condicional. Por ejemplo, 0.0034 Km. 

#### Por otro lado, se incrementará el valor del coeficiente de arrastre tras cada órbita por el ínfimo valor de 0.00005447.

#### Como última anotación, debemos tener en cuenta que vamos a usar el ciclo mientras altactual > altmin para crear el pseudocódigo.