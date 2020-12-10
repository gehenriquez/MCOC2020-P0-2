# MCOC2020-P0
Mi computador principal

Marca/modelo: Hp Pavilion Gaming Laptop 15-dk0xxx

Tipo: Notebook

Año adquisición: 2020

Procesador:
- Marca/Modelo: Intel Core i7-9750H
- Velocidad Base: 2.60 GHz
- Velocidad Máxima: 4.50 GHz
- Numero de núcleos: 6
- Numero de subprocesos: 12
- Arquitectura: Coffe Lake H (64 bits)
- Set de instrucciones: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, EM64T, VT-X, AES, AVX, AVX2, FMA3

Tamaño de las cachés del procesador
- L1d: 32KB  
- L1i: 32KB  
- L2: 256KB   
- L3: 12288KB

Memoria
- Total: 16 GB
- Tipo memoria: DDR4-2667, LPDDR3-2133
- Velocidad 2666 MHz
- Numero de (SO)DIMM: 6
      
Tarjeta Gráfica
- Marca / Modelo: Nvidia GeForce GTX 1660 Ti Max-Q
- Memoria dedicada: 6 GB
- Resolución: 1920 x 1080
      
Disco 1:
- Marca: Toshiba
- Tipo: SSD
- Tamaño: 128 GB
- Particiones: 4
- Sistema de archivos: NTFS
      
Disco 2:
- Marca: Western Digital
- Tipo: SATA 3
- Tamaño: 1TB
- Sistema de archivos: NTFS

Dirección MAC de la tarjeta wifi: 5C-3A-45-A0-52-15

Dirección IP (Interna, del router): 172.24.23.1

Dirección IP (Externa, del ISP): 172.24.23.135

Proveedor internet: roma-penuelas-lapaloma.wifixtreme.cl



# Desempeño MATMUL:
![Para 10 Corridas](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/Plot-10-corridas.png)
- Los graficos difieren principalmente en los tiempos requeridos para hacer las multiplicaciones de las matrices. 

- Probablemente esto sea producto de las diferencias en los procesadores.

- Es lineal porque se utiliza la memoria RAM que funciona de manera mas dinamica, almacenando de a poco para ser utilizado a la brevedad.

- Se esta utilizando la version de python 3.8.5 y version de numypy 1.19.1

- Al correr el programa se utiliza un solo procesador.
![CPU](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

# Desempeño MIMATMUL:

Con el fin de evaluar el rendimiento de la multiplicacion de matrices desarrollado por python (A@B), se elaboró una función que multiplica matrices y se compararon los desempeños de ambas. La función mimatmul((A, B, C) utilizada se muestra a continuación:
def mimatmul(A, B, C):
      N=len(A)
      for m in range(N):
            for j in range(N):
                  for k in range(N):
                        C[m][j] += A[m][k] * B[k][j]
      return C

Lo primero que se observa es que la función de elaboración propia tarda más tiempo en resolver la multiplicacion de matrices pero utilizan la misma memoria para matrices del mismo tamaño. Producto de esta diferencia en los tiempos, se decide usar dos listas de tamaños de matrices, Ns1 = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 10000] y Ns2 = [10, 20, 50, 100, 500, 1000]. El archivo timing_matmul.py es capaz de correr Ns1 y Ns2, tardando no más de 10 min en las 10 corridas, en cambio el archivo mimatmul.py no puede correr Ns1, tras varias horas de correrlo el computador colapso y no entrego los resultados. A continuacion se muestran los Graficos de memoria y tiempo vs tamaño de matrices, para timing_matmul.py con las listas Ns1 y Ns2, y para mimatmul.py se entrega solo con la lista Ns2. 

![Plot-timing_matmul-Ns1](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

![Plot-timing_matmul-Ns2](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

![Plot-mimatmul-Ns2](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

Además se observo en el archivo mimatmul.py, que los tiempos al pasar de matrices de 100 elementos a matrices de 500 elementos aumenta de manera brusca. Para N=100 se utilizan 0.9144420000000001 s y 240000 bytes de memoria, al cambiar a matrices de N=500 se demora 113.51358339999999 s y se necesitan 6000000 bytes. Esto podria ocurrir producto de la memoria requerida, de hecho al observar el segundo grafico se ve como aumenta para todas las multiplicaciones el uso de memoria. Al requerir mas memoria es probable que el procesador no sea capaz de suplir la demanda de memoria de manera dinamica y requiera utilizar mas RAM o en su defecto memoria de disco, por medio de archivos de paginacion. Se muestra tambien los procesadores logicos para los tres escenarios mencionados anteriormente.

![CPU-timing_matmul-Ns1](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

![CPU-timing_matmul-Ns2](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

![CPU-mimatmul-Ns2](https://github.com/gehenriquez/MCOC2020-P0-2/blob/master/Entrega%202/CPU-10-corrida.2.PNG)

Además se subieron los archivos "timing_matmul.py", "mimatmul.py", los archivos "matmul{n}.txt" y "mimatmul{n}.txt" para los 10 archivos de texto (n con valores entre 0 y 9). Todo se desarrollo utilizando la version de python 3.8.5 y la version de numypy 1.19.1.




# Desempeño Ax = b :
- Para matrices de pequeños tamaños el solver que utiliza menos tiempo es el de numpy, para matrices de menos de 10x10. 
- Para tamaños grandes tambien es mas conveniente usar el solver de numpy considerando el tiempo que utiliza, a partir de matrices de tamaño 1000x1000 o mas.
- Para tamaños de N entre 10 y 200 el que requiere menos tiempo es el solver de scipy symmetric y para tamaños de N entre 200 a 1000 el que menos tiempo utiliza para resolver es el solver de scipy pos overwrite.
- se observa una gran variacion de los desempeños de los diferentes solvers a medida que cambian los tamaños de matrices, pero al llegar a matrices de 1000x1000 se empiezan a comportar de manera relativamente parecida.
- Es dificil determinar cual es el con peor desempeño, pero po lo general es el solver de scipy solve.
Además es interesante la variacion en el rendimiento del solve spSolve symmetric, ya que varia significativamente en comparacion a lops demas al cambiar los tamaños dew matrices.

# Matrices dispersas y complejidad computacional :

1- Complejidad algoritmica de MATMUL:
![Para MATMUL llena](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/MATMUL_llena.png)
![Para MATMUL dispersa](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/MATMUL_dispersa.png)

- En general se observa que para MATMUL llena la pendiente es mayor que para el metodo disperso, sobre todo para matrices de tamaños mayores a 50. Al aumentar el tamaño de las matrices se ve un aumento considerable en el tiempo de ensamblado y de solucion para matrices llenas, en cambio para matrices dispersas al aumentar N, se observa solo un aumento en el tiempo de ensamblado.
- Extrañamente el tiempo que se demora en ensamblar y en resolver una matriz llena parece ser menor que el requerido para una dispersa. 
- Se aprecia una buena estabilidad en las corridas.

2- Complejidad algoritmica de SOLVE:
![Para SOLVE llena](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/Solve_llena.png)
![Para SOLVE dispersa](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/Solve_dispersa.png)

- En general se observa que para Solve que para la matriz llena los tiemposde ensamblaje y solucion aumentan considerablemente al aumentar el tamaño de N. En cambio para las matrices dispersas se observa que al aumentar el tamaño de N, el tiempo de ensamblaje aumenta en gran emdida, pero el de solucion no lo hace.
- Extrañamente el tiempo que se demora en ensamblar y en resolver una matriz llena parece ser menor que el requerido para una dispersa. 
- Se aprecia una buena estabilidad en las corridas por lo general, aunque para las matrices llenas, en el tiempo de solicion se ven varios puntos que se escapan de la linea esperada.

3- Complejidad algoritmica de INV:
![Para INV llena](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/INV_llena.png)
![Para INV dispersa](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/INV_disperesa.png)

- Para el caso de INV, se aprecia que los tiempos no aumentan tanto como en los otros casos al trabajar con amtrices mas grandes, para ninguno de los casos. Se observa mas pendiente en las matrices llenas y mas aun en el tiempo de solucion que en el de ensamblaje, pero sigue siendo menor que para los otros metodos. 
- Extrañamente el tiempo que se demora en ensamblar y en resolver una matriz llena parece ser menor que el requerido para una dispersa. 
- Se aprecia una gran estabilidad, podriamos mdecir que es el metodo ams estable. 

## El codigo para las laplacianas es mostrado a continuación:
import numpy as np
from scipy.sparse import lil_matrix, csc_matrix


def matriz_laplaciana_llena(n, t=np.double):
    e = np.eye(n)-np.eye(n, n, 1)
    return t(e+e.T)


def matriz_laplaciana_dispersa(n, t=np.double):
    a = lil_matrix((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i, j] = t(2)
            if (i + 1) == j or (i - 1) == j:
                a[i, j] = t(- 1)
    return csc_matrix(a)
    
- Este codigo es un factor que influye en los resultados, ya que es necesario y se utiliuza en todos los casos y metodos, al hacer una buena seleccion de la funcion laplaciana a utilizar se puede optimizar el tiempo utilizado y ver un aumento en el desempeño del programa. 

