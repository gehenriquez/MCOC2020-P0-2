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
