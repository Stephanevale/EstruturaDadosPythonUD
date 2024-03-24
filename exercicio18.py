class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        self.media = (self.nota1 + self.nota2)/   2
        print(self.media)

    def apro_repro(self):
        if self.media >= 6:
            print('o Aluno está aprovado')
        else:
            print('O aluno está reprovado')

    def resultados(self):
        print('nome: ', self.nome)
        print('nota1: ', self.nota1)
        print('nota2: ', self.nota2)
        print('media: ', self.media)       
        
    

aluno1 = aluno('joão', 10, 9)
aluno1.media()
aluno1.apro_repro()
aluno1.resultados()

aluno2 = aluno('Maria', 8, 7)
aluno2.media()
aluno2.apro_repro()
aluno2.resultados()
