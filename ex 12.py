#UTILIZANDO BRAKE E WHILE TRUE E CONTINUE
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('/ Divisão')
print('* Multiplicação')
print('Pressione outra tecla para sair')



while True:
    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('digite o primeiro valor: '))
        y = int(input('digite o segundo valor: '))

    if op == '+':
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
        continue
    elif op == '-':
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif op == '*':
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif op == '/':
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif(op == 'sair'):
        break
    else:
        print('Operação inválida')

print('ENCERRANDO O PROGRAMA...')