# Write a program that reads a person's full name and then displays the first and last names separately.

name = str(input('Digite seu nome completo: ')).title()

name = name.split()
print(f'Primeiro nome: {name[0]}\nÚltimo nome: {name[-1]}')
