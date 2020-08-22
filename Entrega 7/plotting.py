import numpy as np
import matplotlib.pyplot as plt


N = [2, 5, 10, 15, 20, 30, 45, 50, 60, 75, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000, 8000,16000]

names = ["MATMUL_llena.txt", "MATMUL_dispersa.txt", "Solve_llena.txt", "Solve_dispersa.txt", "INV_llena.txt",
         "INV_disperesa.txt"]
name=[]
for j in names:
    name.append(j)
    xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    yticks = [0.1 / 1000, 1 / 1000, 10 / 1000, 0.1, 1, 10, 60, 600]
    yticks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    xticks_text = ["", "", "", "", "", "", "", "", "", "", ""]
    plt.figure()

    dt1max = []
    dt2max = []
    for i in name:
        data = np.loadtxt(i)
        Ns = data[:, 0]
        dts1 = data[:, 1]
        dts2 = data[:, 2]
        Nsmax = max(Ns)
        dts1max = max(dts1)
        dts2max = max(dts2)

        for i in Ns:
            dt1max.append(max(dts1))
            dt2max.append(max(dts2))

        plt.grid(b=None)
        plt.subplot(2, 1, 1)
        plt.ylabel("Tiempo de ensamblado")
        plt.title(j)
        plt.loglog(Ns, dts1, 'k-o', alpha=0.5, markersize=3)

        plt.yticks(yticks, yticks_text)
        plt.xticks(xticks, xticks_text, rotation=45)
        plt.plot(Ns, dt1max, "--", color="royalblue")
        plt.loglog(Ns, Ns * (dts1max / Nsmax), "--", color="orange")
        plt.loglog(Ns, (Ns ** 2) * (dts1max / (Nsmax ** 2)), "--", color="green")
        plt.loglog(Ns, (Ns ** 3) * (dts1max / (Nsmax ** 3)), "--", color="firebrick")
        plt.loglog(Ns, (Ns ** 4) * (dts1max / (Nsmax ** 4)), "--", color="mediumpurple")
        plt.yticks(yticks, yticks_text)
        plt.xticks(xticks, xticks_text, rotation=45)


        plt.subplot(2, 1, 2)
        plt.loglog(Ns, dts2, 'k-o', alpha=0.5, markersize=3)
        plt.ylabel("Tiempo de solucion")
        plt.xlabel("Tamaño de la matriz")
        plt.yticks(yticks, yticks_text)
        plt.xticks(xticks, xticks, rotation=45)
        plt.grid(b=None)
        plt.plot(Ns, dt2max, "--", color="royalblue", label="Constante")
        plt.loglog(Ns, Ns * (dts2max / Nsmax), "--", color="orange", label="O(N)")
        plt.loglog(Ns, (Ns ** 2) * (dts2max / (Nsmax ** 2)), "--", color="green", label="O(N**2)")
        plt.loglog(Ns, (Ns ** 3) * (dts2max/ (Nsmax ** 3)), "--", color="firebrick", label="O(N**3)")
        plt.loglog(Ns, (Ns ** 4) * (dts2max / (Nsmax ** 4)), "--", color="mediumpurple", label="O(N**4)")
        plt.yticks(yticks, yticks_text)
        plt.xticks(xticks, xticks, rotation=45)

    plt.grid(b=None)
    plt.tight_layout()
    plt.legend()
    plt.show()
    name.pop()

exit(0)
