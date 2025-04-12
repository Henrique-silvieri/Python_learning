# Write a program that reads a person's full name and displays:  
# > - The name with all letters in uppercase;  
# > - The name with all letters in lowercase;  
# > - The total number of letters (excluding spaces);  
# > - The number of letters in the first name.

name = []
name = str(input('Digite seu nome completo: ')).strip()

print(f'\nSeu nome em letras maiúsculas fica : {name.upper()}.')
print(f'\nSeu nome em letras minusculas fica : {name.lower()}.')
print(f'\nSeu nome completo tem {len(name) - name.count(' ')} letras.')
print(f'\nSeu primeiro nome tem {len(name.find(' '))} letras.')
