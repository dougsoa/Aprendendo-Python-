### Criando um help para a função
def soma(x=0, y=0, z=0):
    """
    Retorna o somatório de até 3 valores numéricos quaisquer.
    Todos os parâmetros são opicionais.

    x : valor numérico (opicional).
    y : valor numérico (opicional).
    z : valor numérico (opicional).
    """

    return x + y + z


print(soma(3, 2))
help(soma)
