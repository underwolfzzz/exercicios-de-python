a = int(input("Primeiro lado: "))
b = int(input("Segundo lado: "))
c = int(input("Terceiro lado: "))

if a < b+c or b < a+c or c < b+a:
    if a == b and b == c:
        print("É um trângulo equilatero")
    else: 
        if a == b or b == c or a == c:
            print("É um triangulo isósceles")
        else:
            if a != b and a != c and c != b:
                print("É um triângulo escaleno")
else:
    print("triângulo inválido")