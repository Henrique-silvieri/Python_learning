# Write a program that chooses a number from 0 to 9999 and displays each digit of the number on the screen separately by units, tens, hundreds, and thousands.

number = input('Digite um número entre 0 a 9999: ')

print(f'O número {number} é dividido em:')
print(f'Unidade: {number[3]}')
print(f'Dezena: {number[2]}')
print(f'Centena: {number[1]}')
print(f'Milhar: {number[0]}')
