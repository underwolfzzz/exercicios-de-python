x = 1
soma = 0
qnt = 0
while x != 0:
    x = int(input("Digite o número"))
    if x % 2 == 0:
        soma = soma + x
        qnt = qnt + 1

media = soma / qnt
print(f'A média dos números pares é {media}')