from time import perf_counter
import matplotlib.pyplot as plt
from numpy import *
import numpy as np
from scipy import linalg

def matriz_laplaciana(n):
    A = np.zeros([n,n], dtype = np.double)
    for i in range(n) :
        for j in range(n) :
            if i == j :
                A[i][j] = 2
            elif i == (j+1) or j == (i+1):
                A[i][j] = -1
    return A

Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000]

Ncorridas = 10

for i in range(Ncorridas):
    dts = []
    mem = []

    name = (f"inversa.scipy.True.double{i}.txt")

    fid = open(name, "w")

    for N in Ns:
        print(f"N = {N}")

        A = matriz_laplaciana(N)

        t1 = perf_counter()
        C = linalg.inv(A, overwrite_a=True)
        t2 = perf_counter()

        dt = t2 - t1

        size = 3 * (N ** 2) * C.itemsize

        dts.append(dt)
        mem.append(size)

        fid.write(f"{N} {dt} {size}\n")

        print(f"Tiempo transcurrido = {dt} s")
        print(f"Memoria usada = {size} bytes")

        fid.flush()

    fid.close()

#--------Plotting------------#

colores = ["red","sienna","gray","orange","royalblue","darkseagreen","y","violet","mediumpurple","darkturquoise"]

plt.subplot(2, 1, 1)
for n in range(Ncorridas):
    arch_arreglo = np.loadtxt(f"inversa.scipy.True.double{n}.txt")
    plt.plot(arch_arreglo[:,0],arch_arreglo[:,1], "-o", color=colores[n])
plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xticks_text = ["", "", "", "", "", "", "", "", "", "", ""]

yticks = [0.1 / 1000, 1 / 1000, 10 / 1000, 0.1, 1, 10, 60, 600]
yticks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text)

plt.title("Rendimiento scipy.linalg.inv con overwrite_a=True y np.double")
plt.ylabel("Tiempo transcurrido (s)")
plt.grid()

plt.subplot(2, 1, 2)

plt.plot(arch_arreglo[:,0], arch_arreglo[:,2], '-ob')

plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xticks_text = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

yticks = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 100000000000]
yticks_text = ["1 KB ", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (bytes)")
plt.grid()

plt.show()
