while True:
    try:
        lista = []
        for c in range(0,2):
            valor = float(input(f'Digite um valor: '))
            lista.append(valor)
        divisao = lista[0] / lista[1]
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        print('Ocorreu erro na divisão pois você digitou 0') 
    except IndexError:
        print('Essa posição não existe na lista')
    except KeyboardInterrupt:
        print('A execução foi interrompida')
    else:
        print(f'Os elementos da lista são: {lista}')
        print(f'O valor da divisão é: {divisao}')
        break
