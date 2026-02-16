# Modify the functions that were created in Challenge 107 so that they accept an extra parameter, 
# informing whether the value returned by them will be formatted (by the function created in Challenge 108) or not.

from currency import currency, double, half, increase, decrease

value = float(input('Digite um valor em R$'))
print('')
print(f'o dobro de {currency(value)} é {double(value, True)}.')
print(f'A metade de {currency(value)} é {half(value, True)}.')
print(f'Aumentando em 10%, temos {increase(value, 10, True)}.')
print(f'Reduzindo em 13%, temos {decrease(value, 13, True)}.')
