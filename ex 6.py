# VERDADEIRO OU FALSO PARA NÚMEROS DIVISIVEIS
from datetime import date
ano = int(input('Qual o ano? '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

