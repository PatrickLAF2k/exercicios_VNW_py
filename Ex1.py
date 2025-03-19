# Primeiro Exercício: Soma de elementos pares
# Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
# elementos pares contidos nela.
Exemplo = [2,4,10,3,9,7,15,22]
# Saída: A soma dos pares é: x


def soma_pares (a):
    soma = 0
    for i in a:
        if i % 2 == 0:
            soma += i
    return soma

print(soma_pares(Exemplo))