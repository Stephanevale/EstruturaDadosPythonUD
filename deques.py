#   Combinação de filas e pilhas, podemos remover e adicinar tanto na parte inicial quanto no final
#Suporta operações de pilhas e filas, podemos aplicar em filas de prioridade, agendamento de tarefas de vários processadores.

class Deque:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.inicio = -1
    self.final = 0
    self.numero_elementos = 0
    self.valores = np.empty(self.capacidade, dtype=int) #inicialização do array vazio]

  def __deque_cheio(self): #verifica se o deque já estorou a capacidade
    return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

  def __deque_vazio(self): #indica que o deque está vazio
    return self.inicio == -1

  def insere_inicio(self, valor):
    if self.__deque_cheio():
      print('O deque está cheio')
      return

    # Se estiver vazio
    if self.inicio == -1: #de acordo com a inicialização 
      self.inicio = 0
      self.final = 0
    # Início estiver na primeira posição
    elif self.inicio == 0:
      self.inicio = self.capacidade - 1 #verifica se está do lado direito ou esquerdo
    else:
      self.inicio -= 1
    
    self.valores[self.inicio] = valor #após escontrar o valor colocamos o indice correspondente

  def insere_final(self, valor): #insere valor no final
    if self.__deque_cheio():
      print('O deque está cheio')
      return

    # Se estiver vazio
    if self.inicio == -1:
      self.inicio = 0
      self.final = 0
    # Se final estiver na última posição
    elif self.final == self.capacidade - 1:
      self.final = 0
    else:
      self.final += 1

    self.valores[self.final] = valor

  def excluir_inicio(self):
    if self.__deque_vazio():
      print('O deque já está vazio')
      return

    # Possui somente um elemento
    if self.inicio == self.final:
      self.inicio = -1
      self.final = -1
    else:
      # Volta para a posição inicial
      if self.inicio == self.capacidade - 1:
        self.inicio = 0
      else:
        # Incrementar início para remover o início atual, substitui a posição atual
        self.inicio += 1

  def excluir_final(self):
    if self.__deque_vazio():
      print('O deque já está vazio')
      return
    
    if self.inicio == self.final: #se tiver só um elemento
      self.inicio = -1
      self.final = -1
    elif self.inicio == 0:
      self.final = self.capacidade - 1
    else:
      self.final -= 1 #decrementa o valor

  def get_inicio(self): 
    if self.__deque_vazio():
      print('O deque já está vazio')
      return
    
    return self.valores[self.inicio] #retorna o valor do inicio]

  def get_final(self):
    if self.__deque_vazio() or self.final < 0:
      print('O deque já está vazio')
      return
    
    return self.valores[self.final]
  

  #Criando o objeto da classe

deque = Deque(5)
deque.insere_final(5)
Deque.get_inicio(), Deque.get_final()

deque.insere_final(10)
deque.get_inicio(3), deque.get_final()
deque.get_inicio(2),deque.get_final(11)

#excluir 
deque.excluir_inicio()
deque.excluir_final()

deque.valores #retorna o array

deque.inicio #retorna o indice que está o elemento do inicio

deque.final #retorna o indice do valor que está em formato circular

