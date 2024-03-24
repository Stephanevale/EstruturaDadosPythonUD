dicionario = {}
soma = 0

for c in range(1,4):
    aluno = (input('Digite o nome do aluno: '))
    nota = float(input('Digite a nota: '))
    dicionario[aluno] = nota
    
for elemento in dicionario.values():
    soma+= elemento


print(dicionario)
print(f'A média das notas é: {soma / 3}')