import numpy as np
class pilhas:
    def __init__(self, capacidade):
        self.__capacidade = capacidade #capacidade de armazenamento da pilha
        self.__topo = -1 #indica onde está o topo da pilha, começa com -1 caso o topo esteja vazio
        self.__valores = np.empty(self.__capacidade, dtype= int) #ficará armazenados os valores da pilha

#A ideia da pilha é ter acesso somente ao topo e nã a outros valores
# Para deixar um método privado é necessário colocar dois __ antes do nome do método ex. __def pilha_cheia(self):, dessa forma, ele é acessado somente dentro da classe 

    def __pilha_cheia(self):#ve se a pilha está cheia, função será utilizada quando formos empilhar um elemento
        if self.__topo == self.__capacidade - 1: #-1 pq  os indices em python começam com 0
            return True
        else:
            return False
    
    def __pilha_vazia(self): #ve se a pilha está vazia, função será utilizada quando formos empilhar um elemento
        if self.__topo == -1:
            return True
        else:
            return False
    
    def empilhar(self, valor):
        if self.__pilha_cheia(): #Nesse formato, seria a mesma coisa que if self.__pilha_cheia == True
            print('A pilha está cheia')
        else:
            self.__topo += 1 #encrementa mais um elemento
            self.__valores[self.__topo] = valor
    
    def desempilhar(self): #faz com que o elemento que está no topo saia, o próximo elemento fica no topo
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else: #Nao apaga nenhum elemento, apenas decrementa o topo
            self.__topo -=1
            
    def ver__topo(self):
        if self.__topo != -1: #se a pilha estiver vazia
            return self.__valores[self.__topo] #retorna o valor da posição onde está o topo
        else:
            return -1

pilha = pilhas(5)

pilha.empilhar(1) #adiciona elementos na pilha
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4) #topo da pilha

pilha.desempilhar() #decrementa a pilha do iniciando pelo topo
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver__topo())