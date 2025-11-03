nome = input("Digite o caminho do arquivo: ")
arquivo = open(nome, 'r')

dicionario = {}

for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        palavra = palavra.lower()  # deixa tudo minúsculo pra não diferenciar
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

arquivo.close()

print(dicionario)