import numpy as np
from scipy import linalg
from time import perf_counter
from scipy.sparse.linalg import spsolve, inv
from Matrices_laplacianas import matriz_laplaciana_llena, matriz_laplaciana_dispersa
import matplotlib.pyplot as plt


N = [2, 5, 10, 15, 20, 30, 45, 50, 60, 75, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 8000, 16000]

names = ["MATMUL_llena.txt", "MATMUL_dispersa.txt", "Solve_llena.txt", "Solve_dispersa.txt", "INV_llena.txt",
         "INV_disperesa.txt"]

files = [open(name, "w") for name in names]

for i in N:
    dts1 = np.zeros(len(files))
    dts2 = np.zeros(len(files))
    print(f"N = {i}")

    # --MATMUL matriz llena--

    t1 = perf_counter()
    A = matriz_laplaciana_llena(i)
    B = matriz_laplaciana_llena(i)
    t2 = perf_counter()
    matmul_llena = A @ B
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2
    dts1[0] = dt1
    dts2[0] = dt2

    # ----------------------

    # --MATMUL matriz dispersa--

    t1 = perf_counter()
    A = matriz_laplaciana_dispersa(i)
    B = matriz_laplaciana_dispersa(i)
    t2 = perf_counter()
    matmul_dispersa = A @ B
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2

    dts1[1] = dt1
    dts2[1] = dt2

    # -----------------------

    # --Solve matriz llena--

    t1 = perf_counter()
    A = matriz_laplaciana_llena(i)
    b = np.ones(i, dtype=np.double)
    t2 = perf_counter()
    solve_llena = linalg.solve(A, b)
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2

    dts1[2] = dt1
    dts2[2] = dt2

    # -----------------------

    # --Solve matriz dispersa--

    t1 = perf_counter()
    A = matriz_laplaciana_dispersa(i)
    b = np.ones(i, dtype=np.double)
    t2 = perf_counter()
    solve_dispersa = spsolve(A, b)
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2

    dts1[3] = dt1
    dts2[3] = dt2

    # -----------------------

    # --INV matriz llena--

    t1 = perf_counter()
    A = matriz_laplaciana_llena(i)
    t2 = perf_counter()
    Inv_llena = np.linalg.inv(A)
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2

    dts1[4] = dt1
    dts2[4] = dt2

    # -----------------------

    # --INVtriz dispersa--

    t1 = perf_counter()
    A = matriz_laplaciana_dispersa(i)
    t2 = perf_counter()
    inv_dispersa = inv(A)
    t3 = perf_counter()

    dt1 = t2 - t1
    dt2 = t3 - t2

    dts1[5] = dt1
    dts2[5] = dt2

    # -----------------------

    for j in range(len(files)):
        files[j].write(f"{i} {dts1[j]} {dts2[j]}\n")
        files[j].flush()

[file.close() for file in files]
exit(0)
