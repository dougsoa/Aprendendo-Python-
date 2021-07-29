# APLICANDO O IMPORT RANDOM PARA "SORTEAR" ALEATORIAMENTE
import random
caminhos = ['norte', 'sul', 'leste', 'oeste']
print('O caminho escolhido foi: ' + caminhos [ random.randrange ( len ( caminhos ))])
if caminhos == ['norte', 'sul', 'leste', 'oeste']:
    print('você escapou')
