import numpy as np
matriz = np.array([[2,3,1],[4,5,7]])

#print(matriz)
#print(matriz.shape)
# print(matriz[1])
# print(matriz[0][2])

for i in range(matriz.shape[0]): #estrutura de repetição para as linhas [0]
    print(matriz[i])
    for j in range(matriz.shape[1]): # estrutura de repetição para coluna [1] acessa individualmente os elementos
        print(matriz[i][j])