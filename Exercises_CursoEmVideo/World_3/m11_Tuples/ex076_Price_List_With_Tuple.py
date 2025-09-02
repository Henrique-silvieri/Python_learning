# Create a program that contains a single tuple with product names and their respective prices, in sequence.
# At the end, display a price list, organizing the data in a tabular format.

products = (
    'Pão (1Kg)', 15.90,
    'Leite', 4.20,
    'Arroz (1kg)', 6.80,
    'Feijão (1kg)', 7.30,
    'Café (500g)', 15.90,
    'Queijo', 25.00,
    'Macarrão', 5.50,
    'Molho de tomate', 4.70,
    'Manteiga', 8.60,
    'Ovo (dúzia)', 12.40
)

print('-' * 38)
print ('           Ofertas da Semana')
print('-' * 38)

for product in range(0, len(products), 2):
    print(f'{products[product] :.<30}', end='')
    print(f'R${products[product+1]:>6.2f}')