


import re
#Função search busca a primeira função regular que aparece em um texto.
frase1 = 'Olá, meu número de telefone é (46)0000-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase1))

frase2 = 'A placa de carro é FRT-1998'
print(re.search('[A-Z]{3}-\d{4}', frase2))

email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@\w+\.com', email))

#Função match indica se uma expressão regular está no inicio do texto

frase3 = 'A placa de carro era PRF-1998'
print(re.match('[A-Z]{3}-\d{4}', frase3))
#Aparece None, pois não está no inicio da frase
frase4 = 'FRT-1998 é a placa do carro'
print(re.search('[A-Z]{3}-\d{4}', frase4))

#Função findall busca várias ocorrências
frase5 = 'Olá, meu número atual é (46)0000-0000. O número antigo (55)1111-1111'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase5))

email1 = ''' Nome:  Teste 1
            email: teste@teste.com
            Nome: Teste 2
            email: teste2@teste.com
            Nome: Teste 3
            email: teste3@teste.com.br'''
print(re.findall('\w+@\w+\.\w*', email1))
