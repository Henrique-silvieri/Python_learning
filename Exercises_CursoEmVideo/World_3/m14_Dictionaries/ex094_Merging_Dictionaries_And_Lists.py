# Create a program that reads the name, gender, and age of several people, storing each person’s data in a dictionary 
# and all dictionaries in a list. At the end, display:
# A) How many people were registered.
# B) The average age of the group.
# C) A list containing all women.
# D) A list containing all people whose age is above the average.

people = []
person = {}
sum_age = 0

while True:
    person.clear()
    person['nome'] = str(input('Digite o nome: ')).capitalize()
    
    person['genero'] = str(input('Digite o gênero [M/F]: ')).capitalize()[0]
    while person['genero'] not in 'MmFf':
        del person['genero']
        person['genero'] = str(input('Valor inválido, por favor digite o gênero [M/F]: ')).capitalize()[0]
        
    person['idade'] = int(input('Digite a idade: '))
    sum_age += person['idade']
        
    people.append(person.copy())
    
    continue_ask = str(input('\nDeseja cadastrar outro usuário? [S/N] ')).lower()[0]
    while continue_ask not in 'SsNn':
        continue_ask = str(input('Valor inválido, deseja cadastrar outro usuário? [S/N] ')).strip()[0]
    if continue_ask not in 'SsYy':
        break


print('='*65)

print(f'{len(people)} pessoas foram registradas.')

average_age = sum_age / len(people)
print(f'O grupo tem uma média de {average_age:.2f} anos de idade')    

print(f'As mulheres cadastradas foram: ', end='')
for p in people:
    if p['genero'] in 'Ff':
        print(f'{p['nome']} ', end='')

print(f'\nAs pessoas com idade acima da media são: ')
for p in people:
    if p['idade'] >= average_age:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')

print('='*65)
