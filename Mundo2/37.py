numero = int(input("Digite um numero"))
base = int(input("Qual base de conversão você deseja?\n1-Binário\n2-Octal\n3-hexadecimal"))

if  base == 1:
    resultado = bin(numero)
    print(f"O numero inteiro {numero} em decimal é {resultado[2:]}")
elif   base == 2:
    resultado = oct(numero)
    print(f"O numero inteiro {numero} em octal é {resultado[2:]}")
elif base == 3:
    resultado = hex(numero)
    print(f"O numero inteiro {numero} em hexadecimal é {resultado[2:]}")
else:
    print("numero inválido")
