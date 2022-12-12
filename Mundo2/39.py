import datetime

anoNascimento = int(input("Qual seu ano de nascimento?"))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNascimento

if idade > 18:
    print(f'Voce tem {idade} anos e seu ano de alistamento já passou')
elif idade == 18:
    print(f'Voce tem {idade} anos e precisa se alistar esse ano')
else:
    print(f'Voce tem {idade} anos e precisará se alistar no ano {anoNascimento - idade + 18}')




