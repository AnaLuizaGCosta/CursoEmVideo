import random

x = int(random.randint(0,5))
adv = int(input("Adivinhe o numero de 1 a 5\n\n"))

if  adv <0 or adv>5:
    print("Numero inválido")
else:
    if  adv == x:
        print("Você acertou !")
    else:
        print(f"voce errou, eu pensei no numero {x}")

