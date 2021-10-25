#receber altura e largura de uma parede, calcular a área e quantidade de tinta sendo que 1 l de tinta pinta 2m²
a = float(input('Qual a altura da sua parede em metros? '))
b = float(input('Qual a largura da sua parede em metros? '))
area = a * b
tinta = area / 2
print(f'Sua parede tem área de {area:.1f}m² e precisa de {tinta:.1f} litros de tinta para ser pintada')
