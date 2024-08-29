### Nombre: Jerónimo Jaramillo Rivera

## Diagrama de Bloques
![ctrl + click para abrir la imagen de la primera parte del diagrama](<DIAGRAMA1.png>)

![Segunda parte del diagrama (ctrl+click)](<DIAGRAMA2.png>)
## CASOS:
 ### Módulo de Sensores


#### Velocidad: Número Bits: 10
1. 400 = 0110010000
2. 300 = 0100101100
3. 200 = 0011001000
#### Altitud: Número Bits: 16
1. 10000 =  0010011100010000
2. 20000 =  0100111000100000
3. 500     =  0000000111110100
#### Temperatura: Número Bits: 12
1. 0     = 000000000000
2. 15   = 000000001111
3. 100 = 000001100100
### Módulo de Codificación:  Añade bit de paridad par al final del código, bits de encabezado e iguala cantidad de bits en todos los tipos de datos a 20.
#### Velocidad:  Encabezado: 00  
1. 00000000001100100001
2. 00000000001001011000
3. 00000000000110010001
#### Altitud: Encabezado: 01
1. 00100100111000100000
2. 00101001110001000000
3. 00100000001111101000

#### Temperatura: Encabezado: 11

1. 01100000000000000000
2. 01100000000000011110
3. 01100000000011001001


### Módulo de Decodificación: Verifica la paridad par.

#### Velocidad:  Encabezado: 00  
1. 00000000001100100001
2. 00000000001001011000
3. 00000000000110010001
#### Altitud: Encabezado: 01
1. 00100100111000100000
2. 00101001110001000000
3. 00100000001111101000

#### Temperatura: Encabezado: 11

1. 01100000000000000000
2. 01100000000000011110
3. 01100000000011001001

### Módulo de Conversión Bin2Dec: Convierte la información a código decimal.

#### Velocidad: 
1. 400
2. 300
3. 200 

#### Altitud: 
1. 10000
2. 20000
3. 500    
#### Temperatura: 
1. 0     
2. 15   
3. 100 

### Módulo Cálculo de Error: 
#### SetPoint en ALTITUD = 10 000  
#### SetPoint en VELOCIDAD = 500
#### SetPoint en TEMPERATURA = 35


#### Velocidad: 
1. Error = 400-500= -100
2. Error = 300 -500 = -200
3. Error = 200- 500 = -300
#### Altitud: 
1. Error = 10000- 10000 = 0
2. Error = 20000- 10000 = 10000
3. Error = 500 - 10000 = -9500    
#### Temperatura: 
1. Error = 0 -35 = -35     
2. Error = 15 -35 = -20   
3. Error = 100 - 35 = 65 


### Módulo Conversión Dec2Bin: Convierte los datos de error a binario y mantiene la cantidad de bits igual en todos los datos: Tener en cuenta que el bit de signo es el más significativo.

#### Velocidad: 
1. -100 = 10000000000001100100
2. -200 = 10000000000011001000
3. -300 = 10000000000100101100
##### Altitud: 
1. 10       = 00000000000000001010
2. 10000    = 00000010011100010000
3. -9500    = 10000010010100011100 
#### Temperatura: 
1. -35  =  10000000000000100011 
2. -20  =  10000000000000010100
3. 65   =  00000000000001000001

#### Módulo de Control: Multiplica el error por una constante = 14 = 1110

#### Velocidad: 
 1. 0000000000001100100  * 1110 = 0000000010101111000
 2. 1000000000011001000  * 1110 = 1000000101011110000
 3. 10000000000100101100 * 1110 = 10000001000001101000
#### Altitud: 
1. 00000000000000001010*1110 = 00000000000010001100
2. 00000010011100010000*1110  = 00100010001011100000
3. 10000010010100011100*1110  = 10100000011110001000
#### Temperatura: 
1. 10000000000000100011 *1110= 10000000000111101010
2. 10000000000000010100*1110= 10000000000100011000
3.  00000000000001000001*1110= 00000000001110001110


#### Módulo Codificación CPU: Envía los  datos en binario al módulo de acción de control.


## CONCLUSIONES DE LA ACTIVIDAD: 
#### 1. Aprender sobre la utilidad del sistema binario es necesario para comprender los conceptos más esenciales enla programación, ya que es en este sistema en el que se basan todos los componenetes informáticos contemporáneos, desde un transistor hasta el complejo sistema de sensores de una aeoronave.

#### 2. Es importante conoer los procesos básicos realizados por una computadora para la transmisión de datos; pues facilita detectar y prevenir errores a la hora de programar, además de reconocner la relacion natural entre el hardware y el software.

