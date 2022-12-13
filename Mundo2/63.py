print("="*20)
print("Sequencia Fibonacci")
print("="*20)

termo1 = 0
termo2 = 1
fibonnacci = 0
contador = 1
n = int(input("Quantos termos você quer mostrar?"))
while contador <= n:
    if contador == 1:
        print(f"0 ->", end=" ")
    elif contador == 2:
        print(f"1 ->", end=" ")
    else:
        fibonnacci = termo1 + termo2
        termo1 = termo2
        termo2 = fibonnacci
        print(f"{fibonnacci} ->", end=" ")

    contador += 1
print("FIM")