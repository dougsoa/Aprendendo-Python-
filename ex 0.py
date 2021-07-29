# APLICANDO DESCONTO E UTILIZANDO O FORMAT
produto = float(input('Preço do produto: '))
desc = float(input('Valor do desconto: '))
desconto = (produto * desc)/100
final = produto - desconto
print('O valor do produto R$ {} com desconto de {}% é de R$ {}'. format(produto, desc, final))
