
velocidade = int(input("Qual a velocidade do carro em km/h?\n\n"))
if  velocidade <= 80:
    print("Velocidade dentro do limite")
else:
    multa = (velocidade - 80)*7
    print(f'Você foi multado emR${multa}')