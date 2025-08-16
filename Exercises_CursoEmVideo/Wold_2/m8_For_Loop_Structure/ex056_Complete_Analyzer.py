# Develop a program that reads the name, age, and gender of 4 people. At the end of the program, show:
# -> The average age of the group.
# -> What is the name of the oldest man.
# -> How many women are under 20 years old.

sumAge = 0
averageAge = 0
ageOldestMan = 0
nameOldestMan = ''
womanUnder20 = 0

for i in range(4):
    name = str(input(f'\nDigite o nome da pessoa n°{i+1}: ')).strip().capitalize
    age = int(input(f'Digite a idade da pessoa n°{i+1}: '))
    gender = input(f'Digite o sexo (H/M) da pessoa n°{i+1}: ').strip()
    
    sumAge += age
    
    if i == 1 and gender in 'Hh':
        ageOldestMan = age
        nameOldestMan = name
    
    if gender in 'Hh' and age > ageOldestMan:
        ageOldestMan = age
        nameOldestMan = name
    
    if gender in 'Mm' and age < 20:
        womanUnder20 += 1


averageAge = sumAge/4

print(f'\nA média de idade do grupo é de {averageAge}; \nO homem mais velho do grupo é o {nameOldestMan}, que tem {ageOldestMan} anos; \nO grupo tem {womanUnder20} mulheres com menos de 20 ano.')
