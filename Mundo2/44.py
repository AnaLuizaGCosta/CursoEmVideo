valor = float(input("Valor da compra: R$"))
menu = int(input('''Escolha o Metodo de Pagamento:
[1] - À vista dinheiro/cheque
[2] - À vista cartão
[3] - 2x no cartão
[4] - acima de 3x no cartão
Opção: '''))


if menu == 1:
    pagamento = valor * 0.9
    print(f"Desconto de 10%\nValor total da compra: {pagamento}")
elif menu == 2:
    pagamento = valor * 0.95
    print(f"Desconto de 5%\nValor total da compra: {pagamento}")
elif menu == 3:
    pagamento = valor
    print(f"Valor total da compra: {pagamento}")
    print(f'Valor das parcelas: {pagamento/2}')

elif menu == 4:
    parcelas = int(input("Vai dividir em quantas vezes? "))
    pagamento = valor + valor*0.2
    valorParcelas = pagamento/parcelas
    print(f"Valor total da compra: {pagamento}")
    print(f'Valor das parcelas: {valorParcelas}')
else:
    print("opção inválida")

