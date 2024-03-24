def ler_string(mensagem):
   return  input(mensagem)

def float(numero):
   return numero

mensagem = input(('Digite um texto: '))
numero = float(input(('Digite um numero: ')))
print(f'Você escreveu: {mensagem} e digitou o número: {numero}')