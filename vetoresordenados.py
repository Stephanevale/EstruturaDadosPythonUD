import numpy as np
class vetorordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self. ultima_posicao + 1):
                print(i, '-', self.valores[i]) 
#def O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x-=1
        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar_linear(self,valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1
    #bio log(n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            #se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #se n achou
            elif limite_inferior > limite_superior:
                return -1
            #divide os limites
            else:
                #verifica o limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1 :
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -=1
    
    def insere_ordenado(lista):
        vetor = vetorordenado(len(lista))
        for i in lista:
            vetor.insere[i]
            return vetor
                              

import random
elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))



        
