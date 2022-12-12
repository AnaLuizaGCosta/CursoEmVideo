salario = float(input("Digite seu salário"))

if salario > 1250:
    aumento = salario * 0.1
else: aumento = salario * 0.15

print(f"Voce recebeu um aumento de {aumento}\n Seu novo salário é {salario + aumento}")