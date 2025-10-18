# Create a program that will read several numbers and store them in a list.
# After that, create two additional lists that will contain only the even and the odd values entered, respectively.
# At the end, display the contents of all three generated lists.

numbers = []
numbers_even = []
numbers_odd = []

while True:
    number = int(input('Digite um número para ser adicionado à lista: '))
    
    if number % 2 == 0:
        numbers.append(number)
        numbers_even.append(number)
    else:
        numbers.append(number)
        numbers_odd.append(number)
    
    
    continue_ask = str(input('Você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    while continue_ask not in 'SN':
        continue_ask = str(input('Valor digitado inválido, você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    if continue_ask == 'N':
        break

print(f'Os valores digitados foram {numbers}.')
print(f'Nesta lista tem os seguintes números pares {numbers_even}.')
print(f'Nesta lista tem os seguintes números ímpares {numbers_odd}.')