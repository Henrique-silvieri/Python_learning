# Create a program that reads the birth year of seven people. In the end, show how many people are not yet of legal age and how many are already of legal age. Actual year = 2025
legalAge = 0
notLegalAge = 0
baseYear = 2007

for i in range(7):
    birthYear = int(input(f'Digite o ano de nascimento da pessoa n°{i+1}: '))
    if birthYear <= baseYear:
        legalAge+=1
    else:
        notLegalAge+=1
print(f'Nessa lista tem {legalAge} pessoas maiores de idade e {notLegalAge} pessoas que não são maiores de idade')
