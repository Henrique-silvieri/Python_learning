# Write a program that reads a car's speed. If it exceeds 80 km/h, display a message saying the driver has been fined. The fine will cost R$7.00 for each kilometer over the limit.

speed = float(input('Qual foi a velocidade do veículo em km: '))
if speed <= 80:
    print('Tudo certo!')
else:
    fine = 7 * (speed - 80)
    print(f'Você foi multado por excesso de velocidade, o valor da multa foi de R${fine:.2f}.')
