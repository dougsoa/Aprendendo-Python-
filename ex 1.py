# CALCULOS SIMPLES
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))
apagar = (dias * 60) + (km * 0.15)
print('O carro alugado por {} dias teve {}km percorridos. Portanto o total a pagar será de {}'.format(dias, km, apagar))