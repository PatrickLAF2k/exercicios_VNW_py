# Quarto Exercício: Contagem de Palavras
# Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
# Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
Exemplo = "banana maçã banana laranja maçã maçã";
# Saída: {"banana": 2, "maçã": 3, "laranja": 1}

def contagem_palavras (a):
    lista = a.split()
    contagem = {}
    
    for i in lista:
        contagem[i] = contagem.get(i, 0) + 1
    return contagem

print(contagem_palavras(Exemplo))