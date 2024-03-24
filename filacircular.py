import numpy as np

class Filacircular:
    def __init__ (self,capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype= int)

    def __fila_vazia(self):
        return self.numero_elementos == 0 #retorna true ou false
    
    def __fila_cheia(self): 
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self,valor): 
        if self.__fila_cheia(): #verifica se a fila está cheia
            print('A fila está cheia')
            return
        
        if self.final == self.capacidade -1: #verifica se o inicio da fila está para esquerda ou direita
            self.final = -1 #se chegar a última posição no final do vetor decrementa para ir para a posição 0 novamente
        self.final +=1 
        self.valores[self.final] = valor #indica em qual poisção vai ser inserido o elemento
        self.numero_elementos += 1 #incrementa o número de elemento
    
    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return
        
        temp = self.valores[self.inicio] #indica qual elemento foi desenfileirado iniciando pelo inicio da fila
        self.inicio += 1 
        if self.inicio == self.capacidade: 
            self.inicio = 0
        self.numero_elementos -= 1
        return temp
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]
    

fila = Filacircular(5)

fila.enfileirar(1)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

fila.desenfileirar()
fila.desenfileirar()

fila.enfileirar(6)
fila.enfileirar(7)

print(fila.valores)
print(fila.inicio, fila.final)
print(fila.valores[fila.inicio])