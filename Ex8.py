# Oitavo Exercício: Verificador de Palíndromos
# Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
# pode ser lida da mesma forma de trás para frente) e False caso contrário.
# Exemplo:
# entrada = "radar"
# Saída: True

def palindromo(palavra):
    palavraReversa = "".join(reversed(palavra))
    
    if palavra == palavraReversa:
        return True
    else:
        return False
    
palavra = input("Digite uma palavra: ")
print(palindromo(palavra))