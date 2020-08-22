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
- 
- 
- 
2- Complejidad algoritmica de SOLVE:
- 
- 
- 
3- Complejidad algoritmica de INV:
- 
- 
- 
