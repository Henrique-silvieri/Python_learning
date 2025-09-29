# Create a program where the user can enter several numerical values and store them in a list. 
# If the number already exists in the list, it will not be added. At the end, display all the unique values entered, in ascending order.

values = []
continue_ask = 0
while True:
    number = int(input('Adicione um número à lista: '))
    
    if number not in values:
        values.append(number)
        print('Valor adicionado com sucesso!')
    else: 
        print('Esse número já foi digitado, por favor, tente colocaar outro valor.')
    
    continue_ask = str(input('Você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    
    while continue_ask not in 'SN':
        continue_ask = str(input('Valor digitado inválido, você quer adicionar outro valor a lista (S/N)? ')).strip().upper()[0]
    
    if continue_ask == 'N':
        break

values.sort()
print(f'Os valores inseridos foram: {values}.')