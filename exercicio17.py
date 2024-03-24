import re
numero = 'O número de telefone é (86)8549-7546'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', numero))

cep = 'O número do cep é 64215-345'
print(re.findall('\d{5}\-\d{3}', cep))

urls = 'https://www.udemy.com.br'
print(re.findall('https?://[A-Za-z0-9./]+', urls))