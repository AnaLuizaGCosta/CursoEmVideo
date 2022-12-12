x=float(input("Digite o primeiro numero"))
y=float(input("Digite o segundo numero "))
z=float(input("Digite o terceiro número numero"))

"""if x > y and x > z:
    maior = x
    if y > z:
        menor = z
    else: menor = y

if y > x and y > z:
    maior = y
    if x > z:
        menor = z
    else: menor = x

if z > x and z > y:
    maior = z
    if y>x:
        menor = x
    else: menor = y"""
list = [x,y,z]

print(f"Você digitou {x} , {y}, {z}\n\nO Maior número é {max(list)} e o menor número é {min(list)}")
