# Write a program that reads the year of birth of a young man and, based on his age, informs:
# -> If he will still need to enlist for military service.
# -> If it's time to enlist.
# -> If he is past the enlistment time.
# Your program should also display how many years are left until enlistment or how many years have passed since the deadline.

has_enlisted = input('Você ja cumpriu o alistamento obrigatório? (s/n) ').lower()

if has_enlisted == 's':
    print('Tudo certo, prossiga.')

elif has_enlisted == 'n':
    age = int(input('Quantos anos você tem? '))
    
    if age > 18:
        years_overdue = age - 18
        year_word = "year" if years_overdue == 1 else "years"
        print(f'Já passou {years_overdue} {year_word} da idade necessária para se alistar.')
    
    elif age < 18:
        years_overdue = 18 - age
        year_word = "year" if years_overdue == 1 else "years"
        print(f'Ainda lhe falta {years_overdue} {year_word} para se alistar.')
    
    else:
        print('Você está com a idade necessária para se alistar.')

else:
    print('Resposta inválida tente novamente.')
