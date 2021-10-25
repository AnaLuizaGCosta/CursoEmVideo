'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.'''
import math

n = float(input('Digite o ângulo: '))
nr = math.radians(n)
print(f'Para o ângulo {n}:\nSeu cosseno é {math.cos(nr):.2f}\nSeu Seno é {math.sin(nr):.2f}\nSua Tangente é {math.tan(nr):.2f}')
