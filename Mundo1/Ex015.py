#receba o numero de dias do aluguel do carro e a km rodada e retorne
# o preço a pagar sabendo que o carro custa 60R$ por dia e 0,15/km rodado
dias = int(input('Digite o número de dias de aluguel do carro: R$ '))
km = float(input('Digite os quilômetros rodados durante o aluguel:R$ '))
preço = (dias * 60) + (km * 0.15)
print(f'O valor do aluguel é de R${preço:.2f}')
