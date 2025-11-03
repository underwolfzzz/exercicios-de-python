x = 0
soma = 0
qnt = 0
for x in range (10):
    x = int(input("Digite o número"))
    if x % 2 == 0:
        soma = soma + x
        qnt = qnt + 1

media = soma / qnt
print(f'A média dos números pares é {media}')