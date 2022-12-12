# frase = str(input("Digite uma frase")).upper().replace(" ", "")
# fraseInvertida = ''.join(list(reversed(frase)))
# print(frase)
# print(fraseInvertida)
# if frase == fraseInvertida:
#     print("Sua frase é um Palíndromo")
# else:
#     print("Sua frase não é um Palindromo")



# frase = str(input("Digite uma frase")).upper().replace(" ", "")
# invertida = frase[::-1]
# if frase == invertida:
#     print("Sua frase é um Palíndromo")
# else:
#     print("Sua frase não é um Palindromo")

frase = str(input("Digite uma frase")).upper().replace(" ", "")
invertida = ""
for letra in frase:
    invertida = letra + invertida
if frase == invertida:
    print("Sua frase é um Palíndromo")
else:
    print("Sua frase não é um Palindromo")