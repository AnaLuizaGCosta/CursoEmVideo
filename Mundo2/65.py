
numeros = [int(input("Digite um numero"))]
resposta = str(input("Você deseja finalizar? [S/N]")).strip().upper()

while resposta != 'S':
    numeros.append(int(input("Digite um numero")))
    resposta = str(input("Você deseja finalizar? [S/N]")).strip().upper()

media = sum(numeros)/len(numeros)

print(f'''A média dos numeros foi de {media}
O numero maior foi {max(numeros)}
O numero menor foi {min(numeros)}''')