def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcula a fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i  # fat = fat * 1
    return fat

x = valida_int('Digite um valor para calcular a Fatorial: ', 0, 99999)
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)
