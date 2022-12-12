casaValor = float(input("Informe o valor da casa"))
salario = float(input("Informe seu salario"))
anos = int(input("Informe em quantos anos pretente quitar"))

prestacao = (casaValor/anos)/12

if (salario * 0.3) <= prestacao:
    print(f"O valor da prestação R$ {prestacao:.2f} é incompatível com seu salário\n Pedido: NEGADO")
else:
    print(f"O valor da prestação R$ {prestacao:.2f} é compatível com seu salário\n Pedido: ACEITO")