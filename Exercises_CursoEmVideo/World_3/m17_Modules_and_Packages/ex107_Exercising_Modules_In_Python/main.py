# Create a module named currency.py that has built-in functions for increase(), decrease(), double(), and half().
# Also, create a program that imports this module and uses some of these functions.

from currency import double, half, increase, decrease

value = float(input('Digite um valor em R$'))
print('')
print(f'o dobro de R${value:.2f} é R${double(value):.2f}.')
print(f'A metade de R${value:.2f} é R${half(value):.2f}.')
print(f'Aumentando em 10%, temos R${increase(value, 10):.2f}.')
print(f'Reduzindo em 13%, temos R${decrease(value, 13):.2f}.')