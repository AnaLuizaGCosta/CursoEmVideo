'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
 ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lista = [n1,n2,n3,n4]
r = random.choice(lista)
print(f'O aluno escolhido foi {r}')
