# The National Swimming Confederation needs a program that reads the year of birth of an athlete and displays their category according to their age:
# -> Up to 9 years old: CHILD
# -> Up to 14 years old: YOUTH
# -> Up to 19 years old: JUNIOR
# -> Up to 20 years old: SENIOR
# -> Above 20 years old: MASTER

birthYear = int(input('Qual o ano de nascimento? '))
age = 2025 - birthYear 

if birthYear > 2025:
    print('Ano de nascimento inválido.')
elif age <= 9:
    category = 'MIRIM'
elif age > 9 and age <= 14:
    category = 'JUVENIL'
elif age > 14 and age <= 19:
    category = 'JUNIOR'
elif age == 20:
    category = 'SENIOR'
else:
    category = 'MASTER'

if category:
    print(f"A sua categoria é {category}")