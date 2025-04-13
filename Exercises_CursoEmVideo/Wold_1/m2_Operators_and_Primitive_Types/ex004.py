# Create a program that reads something from the keyboard and displays on the screen its primitive type and all possible information about it.

x = input('digite algo: ')
print(f'O tipo primitivo do valor digitado é {type(x)}')
print(f'Só tem espaços? {x.isspace}')
print(f'É um número? {x.isnumeric}')
print(f'É alpha numérico? {x.isalnum}')
print(f'Está em maiúsculo? {x.isupper}')
print(f'Está em minúsculo? {x.islower}')
print(f'Está capitalizada? {x.istitle}')
