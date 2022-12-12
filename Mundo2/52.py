numero = int(input("Digite um numero"))
divisores = 0
for contador in range(1,numero+1):
    if numero % contador == 0:
        divisores += 1
        # print(f"contador: {contador}")
        # print(f"divisores: {divisores}")
if divisores == 2:
    print(f"Seu número {numero} é primo")
else:
    print(f"Seu numero {numero} não é primo")