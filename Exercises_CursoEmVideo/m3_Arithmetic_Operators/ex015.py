# Write a program that reads the number of kM driven by a rented car and the number of days it was rented. Calculate the total price to be paid, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

days = int(input('Por quantos dias o carro foi alugado? '))
km_driven = float(input('Qual foi a distância em Km, em que o carro percorreu? '))
price = (km_driven * 0.15) + (days * 60)

print(f'O preço final a ser pago,considerando que o carro foi alugado por {days} dias e percorreu {km_driven} Km é de R${price:.2f}')
