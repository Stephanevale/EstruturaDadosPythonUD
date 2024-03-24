def  retorna_valor_temperatura():
   return int(input('Temperatura em C°: '))
  

def faz_conversao(temperatura):
   return (9 * temperatura + 160) / 5
    

def mostra_resultado(temperatura):
    print(f'O resultado da conversão é {temperatura}')

temperatura_c = retorna_valor_temperatura()
temperatura_em_fahrenheit = faz_conversao(temperatura_c)
mostra_resultado(temperatura_em_fahrenheit)