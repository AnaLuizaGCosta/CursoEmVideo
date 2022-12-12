pessoas = []
idades = []
sexo = []
pessoasHomens = []
idadeHomens = []
pessoasMulheres = []
idadeMulheres = []

for atributos in range(0,4):
    print("-"*20, end="")
    print(f"Pessoa {atributos+1}", end="")
    print("-"*20)
    pessoas.append(str(input("Nome:")))
    idades.append(int(input("Idade")))
    sexo.append(str(input("[M/F]?")))
    if sexo[atributos] == "M":
        pessoasHomens.append(pessoas[atributos])
        idadeHomens.append(idades[atributos])
    else:
        pessoasMulheres.append(pessoas[atributos])
        idadeMulheres.append(idades[atributos])


print(pessoas, idades, sexo)
print(pessoasHomens, pessoasMulheres)
print(idadeHomens, idadeMulheres)
print(f"A media de idades é de {sum(idades)/len(idades)}")

homenMaisVelho = idadeHomens.index(max(idadeHomens))
print(f"O {pessoasHomens[homenMaisVelho]} é o homem mais velho")

mulheresComMenosde20 = 0

for mulher in idadeMulheres:
    if mulher < 20:
        mulheresComMenosde20 +=1
print(f"São {mulheresComMenosde20} mulheres com menos de 20 anos")

