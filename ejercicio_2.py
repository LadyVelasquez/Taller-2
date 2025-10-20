import numpy as np

coeficientes = [1, 6, 1]
raices = np.roots(coeficientes)

print(f"Las raices del polinomio son: \n {raices}\n")
print(f"Los puntos de intersección de la curva son: \n ({raices[0]},-2) ({raices[1]}, -2) ")
