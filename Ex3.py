# Terceiro Exercício: Contagem de Frequência
# Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
# caracteres da string e os valores representam quantas vezes cada caractere aparece.
Exemplo = ["Java", "Java", "Ruby", "Javascript", "Ruby"];
# Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}

def contagem_ferquencia (a):
    frequencia = {}
    for i in a:
        frequencia[i] = frequencia.get(i, 0) + 1
    return frequencia

print(contagem_ferquencia(Exemplo))