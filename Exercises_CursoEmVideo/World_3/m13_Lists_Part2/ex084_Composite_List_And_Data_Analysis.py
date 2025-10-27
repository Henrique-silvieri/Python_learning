# Create a program that reads the name and weight of several people, storing everything in a list.
# At the end, display:
# A) How many people were registered.
# B) A list containing the heaviest people.
# C) A list containing the lightest people.

haviest = lightest = 0
people = []
data = []

while True:
    data.append(str(input('Digite o nome: ')))
    data.append(float(input('Digite o peso (Kg): ')))
    
    if len(people) == 0:
        haviest = lightest = data[1]
    else:
        if data[1] > haviest:
            haviest = data[1]
        if data[1] < lightest:
            lightest = data[1]
    
    people.append(data[:])
    data.clear()
    
    
    continue_ask = str(input('Você quer adicionar outra pessoa (S/N)? ')).strip().upper()[0]
    while continue_ask not in 'SN':
        continue_ask = str(input('Valor digitado inválido, você quer adicionar outra pessoa (S/N)? ')).strip().upper()[0]
    if continue_ask == 'N':
        break

print(f'\nVocê adicionou {len(people)} pessoas.')
print(f'O maior peso foi {haviest}Kg. Peso de', end='')
for person in people:
    if person[1] == haviest:
        print(f'[{person[0]}]', end=' ')
        
print(f'O menor peso foi {lightest}Kg. Peso de ', end='')
for person in people:
    if person[1] == lightest:
        print(f'[{person[0]}]', end=' ')
