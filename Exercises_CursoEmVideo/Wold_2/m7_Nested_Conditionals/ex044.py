# Write a program that calculates the amount to be paid for a product, considering its regular price and the chosen payment method:
# -> Cash payment (cash/check): 10% discount
# -> Immediate payment by card: 5% discount
# -> Up to 2 installments on the card: regular price
# -> 3 or more installments on the card: 20% interest

initialPrice = float(input('Qual o preço do produto? '))
paymentMethod = int(input('Qual a forma de pagamento? (digite o número que corresponda a opção do cliente) \n1 - à vista (dinheiro/cheque) \n2 - à vista no cartão \n3 - parcelado no cartão \n\n'))

if paymentMethod == 1:
    finalPrice = initialPrice - (initialPrice*0.1)
    print(f'O pagamento à vista no dinheiro/cheque tem 10% de desconto! Portanto o valor total da compra é de R${finalPrice:.2f}.')

elif paymentMethod == 2:
    finalPrice = initialPrice - (initialPrice*0.05)
    print(f'O pagamento à vista no cartão tem 5% de desconto! Portanto o valor total da compra é de R${finalPrice:.2f}.')

elif paymentMethod == 3:
    installmentsNumber = int(input('Em quantas vezes deseja parcelar? (mínimo de 2x) '))
    
    if installmentsNumber == 2:
        finalPrice = initialPrice / 2
        print(f'O valor da compra desta opção é de 2x de R${finalPrice:.2f}.')
    
    elif installmentsNumber > 2:
        finalPrice = (initialPrice + initialPrice * 0.1) / installmentsNumber
        print(f'O pagamento com {installmentsNumber} parcelas tem um juros de 10%! Portanto o valor total da compra é de {installmentsNumber}x de R${finalPrice:.2f}.')

    else:
        print('Ops! Parece que essa opção não existe. Tente novamente')

else:
    print('Ops! Parece que essa opção não existe. Tente novamente')
