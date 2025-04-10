# Make a program that reads the price of a product and shows its new price with a 5% discount.

price = float(input('Digite o preço do produto (R$):'))
discount = price - (price * 0.05)

print(f'O novo preço com 5% de desconto fica R${discount:.2f}.')
