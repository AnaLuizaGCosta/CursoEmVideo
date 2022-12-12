distancia = float(input("Qual a distância da viagem em km/h?\n"))
if distancia <= 200:
    passagem = (0.5 * distancia)
else:
    passagem = (0.45 * distancia)

print(f"Valor da passagem: {passagem:.2f}")
