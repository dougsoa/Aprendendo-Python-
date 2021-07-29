#UTILIZANDO WHILE PARA LOOPING NA CALCULADORA
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('/ Divisão')
print('* Multiplicação')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('digite o primeiro valor: '))
    y = int(input('digite o segundo valor: '))

while op != 'sair':
    if op == '+':
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
    elif op == '-':
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif op == '*':
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif op == '/':
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
    else:
        print('Operação inválida')

    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('digite o primeiro valor: '))
        y = int(input('digite o segundo valor: '))

print('ENCERRANDO O PROGRAMA...')