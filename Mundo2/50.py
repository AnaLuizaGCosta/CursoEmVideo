lista = []
for cont in range(1, 7):
    valor = int(input('Digite um numero'))
    if valor%2 == 0:
        lista.append(valor)
print(lista)
print(sum(lista))

# soma = 0
# for count in range(1,7):
#     valor = int(input('Digite um numero'))
#     if valor%2 ==0:
#         soma += valor
# print(soma)