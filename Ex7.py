# Sétimo Exercício: Top 3 mais frequentes
# Dada uma lista de números, crie uma função que retorne os três números mais frequentes
# em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.
Exemplo = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
# Saída: [2, 1, 4]

def frequentes(a):
    contagem = {}  # Inicializa o dicionário para contar as ocorrências

    for i in a:
        if i in contagem:  # Se a chave já existe, soma 1
            contagem[i] += 1
        else:  # Se a chave não existe, inicializa com 1
            contagem[i] = 1

    # Ordena primeiro por frequência (decrescente) e depois pelo número (crescente)
    mais_frequentes = sorted(contagem.keys(), key=lambda x: (-contagem[x], x))

    return mais_frequentes[:3]  # Retorna os 3 mais frequentes

print(frequentes(Exemplo))