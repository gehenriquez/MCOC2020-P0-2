# MCOC2020-P0
Mi computador principal

Marca/modelo: Hp Pavilion Gaming Laptop 15-cx0xxx

Tipo: Notebook

Año adquisición: 2018

Procesador:
- Marca/Modelo: Intel Core i5-8300H
- Velocidad Base: 2.30 GHz
- Velocidad Máxima: 4.00 GHz
- Numero de núcleos: 4
- Humero de hilos: 8
- Arquitectura: x64-based PC
- Set de instrucciones: 64-bit

Tamaño de las cachés del procesador
- L1d: 32KB
- L1i: 32KB
- L2: 256KB
- L3: 8192KB

Memoria
- Total: 8 GB
- Tipo memoria: DDR4-2666, LPDDR3-2133
- Velocidad 1330 MHz
- Numero de (SO)DIMM: 4.
      
Tarjeta Gráfica
- Marca / Modelo: Nvidia GeForce GTX 1050
- Memoria dedicada: 8192 MB
- Resolución: 1920 x 1080
      
Disco 1:
- Marca: Seagate Mobile
- Tipo: HDD
- Tamaño: 1TB
- Particiones: 4
- Sistema de archivos: EXT4.

Dirección MAC de la tarjeta wifi: 74:40:BB:38:7F:83

Dirección IP (Interna, del router): 192.168.100.151

Dirección IP (Externa, del ISP): 181.43.56.30

Proveedor internet: Entel Chile



# Desempeño MATMUL:
- Los graficos difieren principalmente en los tiempos requeridos para hacer las multiplicaciones de las matrices. 
- Probablemente esto sea producto de las diferencias en los procesadores.
- Es lineal porque se utiliza la memoria RAM que funciona de manera mas dinamica, almacenando de a poco para ser utilizado a la brevedad.
- Se esta utilizando la version de python 3.8.5 y version de numypy 1.19.1
- Al correr el programa se utiliza un solo procesador, se puede ver en el archivo adjuntado con nombre "procesador.PNG".

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
![Para INV disperesa](https://github.com/gehenriquez/MCOC2020-P0/blob/master/Entrega%207/INV_dispersa.png)
-Para el caso de INV, se aprecia que los tiempos no aumentan tanto como en los otros casos al trabajar con amtrices mas grandes, para ninguno de los casos. Se observa mas pendiente en las matrices llenas y mas aun en el tiempo de solucion que en el de ensamblaje, pero sigue siendo menor que para los otros metodos. 
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

