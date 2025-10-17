# Create a program that will read several numbers and store them in a list. After that, display:
# A) How many numbers were entered.
# B) The list of values, sorted in descending order.
# C) Whether the number 5 was entered and is present in the list.

numbers = []
i = count = 0

while True:
    number = int(input('Adicione um número à lista: '))    
    numbers.append(number)

    count += 1    
    continue_ask = str(input('Você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    
    while continue_ask not in 'SN':
        continue_ask = str(input('Valor digitado inválido, você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    
    if continue_ask == 'N':
        break

numbers.sort()
numbers.reverse()
print(f'{numbers}')
print(f'A lista tem {len(numbers)} digitos')
print(f'O valor 5 está na posição: {numbers.index(5)}')