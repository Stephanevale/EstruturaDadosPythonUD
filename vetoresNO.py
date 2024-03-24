import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade): #capacidade  máxima do vetor
        self.capacidade = capacidade  
        self.ultima_posicao = -1 #armazena onde está o último elemento do vetor
        self.valores = np.empty(self.capacidade, dtype=float)  #aqui teremos os dados do vetor, retorna um novo arrey, dtype pode  ser uma classe, int, float..
    def imprimi(self): #função para imprimir os valores dos vetores, big o - O(n) (percorre de acordo com a quantidade de elementos)
        if self. ultima_posicao == -1: #incrementar a variável toda vez que acrescentar um novo elemento no vetor
            print('O vetor está vazio')
        else: 
            for i in range(self.ultima_posicao +1): #percorre todos os elementos do vetor, apenas as posições que estão sendo ocupadas, 
                print(i,'-', self.valores[i]) #valores na posição i
    def insere(self, valor): #função para receber um valor no vetor big O - O(1) ou O(n) função constante
        if self.ultima_posicao == self.capacidade - 1:
            print('capacidade máxima já foi atingida') #verifica a última posição, para não gerar erros de indice
        else:
            self.ultima_posicao += 1 #incrementa mais um valor no vetor
            self.valores[self.ultima_posicao] = valor #incrementa um valor na ultima posição
    def pesquisar(self, valor): #função para pesquisar o valor, big-o o(n) linear
        for i in range(self.ultima_posicao +1): 
            if valor == self.valores[i]: #compara o valor passado com o valor armazenado no vetor
                return i #retorna em qual posição foi encontrado
        return -1 #quer dizer que o elemento não existe no vetor
    def excluir(self, valor): #função de excluir, big-o o(n)
        posicao = self.pesquisar(valor) #primeiro precisa pesquisara para saber se o valor existe no vetor
        if posicao == -1: #se a posicao for a -1, ou seja, se não existe
            return -1
        else: #condição que inicia de onde foi encontrado o valor até a última posição do vetor
            for c in range(posicao, self.ultima_posicao):
                self.valores[c] = self.valores[c + 1] #faz o remanejamento de uma posição para outra
            self.ultima_posicao -= 1 #atualiza a quantidade de posições ocupadas

import random
elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))

def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
        return vetor
    
(insere_nao_ordenado(elementos))
# vetor = VetorNaoOrdenado(5) #passa  valor da capacidade do vetor
# vetor.insere(2) #insere valores na última posição
# .imprimi() #mostra a mensagem
