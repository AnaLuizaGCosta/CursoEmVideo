print("="*20)
print("Termos de uma PA")
print("="*20)

a = int(input("Primeiro termo: "))
r = int(input("razão: "))

for n in range(1,11):
    an = a + (n -1)*r
    print(an,"->", end=" ")
print("ACABOU!")