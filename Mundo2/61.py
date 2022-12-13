print("="*20)
print("Termos de uma PA")
print("="*20)

a = int(input("Primeiro termo: "))
r = int(input("razão: "))
n = 1
while n < 11:
    an = a + (n - 1) * r
    if n<10:
        print(an, "->", end=" ")
    else:
        print(an,"", end="")
    n += 1
