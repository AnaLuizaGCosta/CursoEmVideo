'''Faça um programa que leia o comprimento do cateto oposto e do cateto
 adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa'''
from math import hypot
# metodo 1

ad = float(input('Digite o cateto adjacente: '))
op = float(input('Digite o cateto oposto: '))
hip = (ad ** 2 + op ** 2) ** 0.5
print(f'O cateto adjacente é {ad:.2f}, o caeto oposto é {op:.2f} e a hipotenusa é {hip:.2f}')

#metodo 2

ad2 = float(input('Digite o cateto adjacente: '))
op2 = float(input('Digite o cateto oposto: '))
hip2 = hypot(ad2,op2)
print(f'O cateto adjacente é {ad2:.2f}, o cateto oposto é {op2:.2f} e a hipotenusa é {hip2:.2f}')
