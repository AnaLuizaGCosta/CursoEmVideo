import datetime

idade=0
aniversarios = []
maiores = 0
menores = 0

for pessoa in range(1,8):
    aniversarios.append(int(input(f"DIgite a data de nascimento da pessoa {pessoa}: ")))
    idade = datetime.date.today().year - aniversarios[pessoa-1]
    if idade >18:
        maiores += 1
    else:
        menores +=1


print(f"São {maiores} maiores de idade e {menores} menores de idade")