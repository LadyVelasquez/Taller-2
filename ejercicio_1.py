import numpy as np

coeficientes = [1, 540, 109124, 9781632, 328188672]
raices = np.roots(coeficientes)

print("Las raices del polinomio son: \n", raices)