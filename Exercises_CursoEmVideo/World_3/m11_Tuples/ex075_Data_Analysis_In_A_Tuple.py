# Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, display:
# A) How many times the value 9 appeared.
# B) In which position the first value 3 was entered.
# C) Which numbers are even.

numbers = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: '))
)
value9 = first_time3 = 0
numbers_evens = [n for n in numbers if n % 2 == 0]

for number in numbers:
    print(f'{number} ', end='')

print(f'\nO valor 9 aparece na primeira vez na posição {numbers.index(9)}.')
print(f'O número 3 aparece {numbers.count(3)} vezes.')
if numbers_evens:
    print(f'Os numberos pares são: {numbers_evens}')
else:
    print('Não há nenhum número par.')
