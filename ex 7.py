#UTILIZANDO O IF, AND E O ELSE
a = int(input('escolha o 1° lado do triangulo: '))
b = int(input('escolha o 2° lado do triãngulo: '))
c = int(input('escolha o 3° lado do triângulo: '))

if (a > 0) and (b > 0) and (c > 0):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a != b and a != c and b != c:
            print('Triangulo escaleno')
        else:
            if a == b and a == c and b == c:
                print('Triangulo equilátero')
            else:
                print('triangulo isóseles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triangulo')

else:
     print('Ao menos um dos valores indicados não servem para formar um triangulo')