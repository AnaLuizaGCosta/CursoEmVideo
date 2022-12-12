import random

list = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(list)

print('''Vamos Jogar JOKENPO!
escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Opção: '))

print(f'''Você escolheu: {list[jogador]}
Eu escolhi: {comp}''')

if jogador == 0:
    jogador = str('Pedra')
    if comp == 'Pedra':
        print('Empate !!')
    elif comp == 'Papel':
        print('Você perdeu !!')
    else:
            print('Você ganhou!!')

elif jogador == 1:
    jogador = str('Papel')
    if comp == 'Pedra':
        print('Você ganhou!!')
    elif comp == 'Papel':
        print('Empate !!')
    else:
            print('Você perdeu !!')

elif jogador == 2:
    jogador = str('Tesoura')
    if comp == 'Pedra':
        print('Você perdeu !!')
    elif comp == 'Papel':
        print('Você ganhou!!')
    else:
        print('Empate !!')
else:
    print("Opção invalida")


