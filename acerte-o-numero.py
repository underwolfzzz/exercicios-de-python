n = int(input("Digite o número imaginado: "))
chute = 0
while chute != n:
    chute = int(input("Chute um número: "))
    if chute > n:
        print("Chute alto")
    if chute < n:
        print("Chhute baixo")

print("Chute correto!")