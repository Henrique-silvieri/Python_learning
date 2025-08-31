# Create a program that reads the age and gender of multiple people. After each person is registered, the program should ask the user whether they want to continue or not. At the end, display:
# A) How many people are over 18 years old.
# B) How many men were registered.
# C) How many women are under 20 years old.

total_people = people_over_18 = men_count = women_under_20 = 0
while True:
    age = int(input('\nDigite a idade do usuário: '))
    
    gender = ' '
    while gender not in 'HM':
        gender = str(input('Digite o gênero do usuário (H/M): ')).strip().upper()[0]
    
    if age > 18:
        people_over_18+=1
    if gender == 'H':
        men_count+=1
    if gender == 'M' and age < 20:
        women_under_20+=1
    
    total_people+=1
    
    continue_answer = ' '
    while continue_answer not in 'SN':
        continue_answer = str(input('Deseja cadastrar outro usuário (S/N)? ')).strip().upper()[0]

    if continue_answer == 'N':
        break

print(f'Com um total de {total_people} usuário(s) cadastrado(s), constam {people_over_18} usuário(s) com mais de 18 anos de idade,', end='')
print(f' {men_count} homem(s) e {women_under_20} mulher(es) com menos de 20 anos de idade')