import random

numeroNPC = random.randint(0, 10)
numeroUser = int(input("Digite um numero"))

while numeroNPC != numeroUser:
    if numeroNPC > numeroUser:
        numeroUser=int(input("Mais.. Tente mais uma vez :)"))
    else:
        numeroUser = int(input("Menos... Tente de novo :)\n"))


print(f"Eu pensei no numero {numeroNPC}\nVocê pensou no numero {numeroUser}")
