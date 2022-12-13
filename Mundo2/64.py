soma = 0
contador = 0
numero = int(input("Digiten um número"))

while numero != 999:
    soma += numero
    contador +=1
    numero = int(input("Digiten um número"))

print(f'''soma = {soma}
Contador = {contador}''')
