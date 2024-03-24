alunos = {}
while True:
    nome = input('digite o nome do aluno: ')
    nota = int(input('digite a nota do aluno: '))
    continuar = input('Quer continuar? S/N: ')
    alunos[nome] = nota
    if continuar == 'N' or continuar == 'n':
        break
    else:
        nome
        nota

with open('alunos.text','w') as texto:
    for alunos, nota in alunos.items():
        texto.write(f'{alunos}, {nota}\n')

with open('alunos.text', 'r') as texto:
    for linha in texto:
        print(linha)

