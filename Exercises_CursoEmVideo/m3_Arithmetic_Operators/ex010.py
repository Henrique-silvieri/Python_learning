# Create a program that reads the amount of money a person has in their wallet and displays how many dollars they can buy. Assume that US$1.00 = R$6.10.

money = float(input('Quandos reais você tem em sua carteira? '))
dollar = money / 6.1
print(f'Com R${money:.2f}, você consegue comprar: US${dollar:.2f}')
