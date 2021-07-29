# USANDO LEN E INT PARA "CORTAR" FRASES
frase = input('Digite uma frase: ')
tam = len(frase)
frase1 = frase[:int(tam/2)]
print(frase1[-2:])
