# Adapt the code from Challenge 107, creating an additional function called moeda() that is capable of showing the values 
# as a formatted currency value.

from currency import currency, double, half, increase, decrease

value = float(input('Digite um valor em R$'))
print('')
print(f'o dobro de {currency(value)} é {double(value)}.')
print(f'A metade de {currency(value)} é {half(value)}.')
print(f'Aumentando em 10%, temos {increase(value, 10)}.')
print(f'Reduzindo em 13%, temos {decrease(value, 13)}.')
