lista = []
soma = 0

for c in range(1,6):
    numero = int(input(f'Digite {c}º número: '))
    soma += numero
    lista.append([numero])
        
print(f'Os valores da lista foram: {lista}')
print(f'A soma dos valores da lista é: {soma}')