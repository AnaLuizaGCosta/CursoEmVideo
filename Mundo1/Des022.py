''' Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(f'O nome tem {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
