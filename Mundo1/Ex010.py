#leia a quantidade em reais e converta para dolar = 3,27R$
real = float(input('Quanto dinheiro você tem na carteira?: R$3.27'))
dolar = real / 3.27
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
