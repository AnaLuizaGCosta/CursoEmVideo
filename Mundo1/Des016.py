# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# método 1
from math import trunc

n = float(input('Digite um número: '))

print(f'Seu número é {n} e sua fração inteira é {trunc(n)}')

# métdo 2

n2 = float(input("Digite um número:"))

print(f'Seu número é {n2} e sua porção inteira é {int(n2)}')

