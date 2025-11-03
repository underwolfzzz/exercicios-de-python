numeros = [1, 2, 3, 4, 5]
menores = []
for n in numeros:
    if n < 4:
        menores.append(n)
print(menores)

menores2 = [n for n in numeros if n < 4]
print(menores2)