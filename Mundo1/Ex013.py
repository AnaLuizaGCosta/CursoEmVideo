# Ler um salário e retornar com 15% de aumento
s = float(input('Qual o salário do funcionário?: '))
sa = s + (s * (15/100))
print(f'O salário de {s:.2f}$ com 15% de aumento subirá para {sa:.2f}$')
