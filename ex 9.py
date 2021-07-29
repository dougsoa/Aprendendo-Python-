# UTILIZANDO O IF, ELSE E ELIF
kwh = float(input('Quantos kwh? '))
tipo = input('Qual o tipo de instalação (R, C ou I): ')

if (tipo == 'r'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'c'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'i'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Instalação inválida!')

print('Total a pagar {:.2f}'.format(kwh * preco))