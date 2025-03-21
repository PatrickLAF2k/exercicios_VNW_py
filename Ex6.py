# Sexto Exercício: Combinação de dicionários
# Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
# inteiros. A função deve combinar os dicionários somando os valores das chaves que
# aparecem em ambos.
# Exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
# Saída: {"a": 3, "b": 7, "c": 5, "d": 7}

def soma_dicionarios (a, b):
    dicionario = a
    
    for key, valor in b.items():
        a[key] = a.get(key, 0) + valor
    return dicionario

print(soma_dicionarios(d1, d2))