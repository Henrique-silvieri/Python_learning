# Write a program that asks for the distance of a trip in kilometers. Calculate the ticket price, charging R$0.50 per kilometer for trips up to 200 km and R$0.45 for longer trips.

distance = float(input('Qual é a distância da viagem em questão? '))

if distance <= 200:
    price = distance * .5
else:
    price = distance * .45

print(f'O preço da viagem é de R${price:.2f}')
