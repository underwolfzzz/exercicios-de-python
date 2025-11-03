print("1 - Tabuada de um número")
print("2 - Calcular IMC")
print("3 - Calcular Fatorial")
print("-1 - Sair")

def tabuada(num):
    if 1 <= num <= 9:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("Erro: o número é inválido")


def imc(peso, h):
    imc_val = peso / (h * h)
    return imc_val


def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat = fat * i
    return fat

opcao = int(input("Escolha uma opção: "))

while opcao != -1:

    if opcao == 1:
        n = int(input("Digite um número: "))
        tabuada(n)

    elif opcao == 2:
        peso = float(input("Digite seu peso : "))
        h = float(input("Digite sua altura: "))
        result = imc(peso, h)
        print(f"Seu IMC é: {result}")

    elif opcao == 3:
        n = int(input("Digite um número: "))
        result = fatorial(n)
        print(f"O fatorial de {n} é {result}")
        
    else:
        opcao = int(input("Opção inválida! Tente novamente."))