print("="*20)
print("Termos de uma PA")
print("="*20)

a = int(input("Primeiro termo: "))
r = int(input("razão: "))
n = 0
maisTermos = 1
total = 10
while maisTermos !=0:
    total += n
    while n < total:
        an = a + (n - 1) * r
        print(an, "->", end=" ")
        n += 1
    print("PAUSA")
    total = int(input("Quantos termos mais você gostaria de mostrar?"))
    maisTermos = total

print(f"Foram mostrados {n} termos")