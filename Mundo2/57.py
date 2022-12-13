# sexo = str()
#
# while sexo != "M" and sexo !="F":
#     sexo = str(input("Qual seu sexo? [F/M]")).strip().upper()[0]

sexo = str(0)
while sexo not in 'MmFf':
    sexo = str(input("Qual seu sexo? [F/M]")).strip().upper()[0]
print(f"Sexo [{sexo}] registrado com sucesso")