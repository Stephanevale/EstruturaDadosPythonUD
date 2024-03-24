import numpy as np
soma = 0

matriz = np.array([[4,3,1],
                   [3,1,5]])

for elemento in matriz[0]:
    soma += elemento
for valor in matriz[1]:
    soma += valor

soma += 0  


print(soma)
