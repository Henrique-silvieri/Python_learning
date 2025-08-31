# # Create a program that reads the name and the price of multiple products. The program should ask the user whether they want to continue or not. At the end, display:
# A) The total amount spent on the purchase.
# B) How many products cost more than R$1000.
# C) The name of the cheapest product.

total_price = products_more_than_1000 = count = cheapest_product = 0
cheapest_name = ''

while True:
    product_name = str(input('Digite o nome do produto: '))
    product_price = float(input('Digite o preço do produto: R$'))
    
    total_price += product_price
    count += 1
    
    if product_price > 1000:
        products_more_than_1000 += 1
    
    if count == 1 or product_price < cheapest_product:
        cheapest_product = product_price
        cheapest_name = product_name
    
    continue_awnser = ' '
    while continue_awnser not in 'SN':
        continue_awnser = str(input('Deseja adicionar outro produto (S/N)? ')).strip().upper()[0]
    
    if continue_awnser == 'N':
        break

print(f'A compra teve um total de R${total_price:.2f}.')
print(f'Teve {products_more_than_1000} produtos que custaram mais de R$1000.00.') 
print(f'O produto mais  barato foi: {cheapest_name} que custa R${cheapest_product:.2f}.')