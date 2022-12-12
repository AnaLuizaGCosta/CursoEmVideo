pesos =[]

for peso in range(1,6):
    pesos.append(float(input(f"Digite o peso da pessoa {peso}")))

print(f"O peso maior é: {max(pesos)}Kg")
print(f"O peso menor é: {min(pesos)}Kg")
