# Create a program where the user can enter five numerical values and store them in a list, already in the correct insertion position 
# (without using sort()). At the end, display the ordered list on the screen.

numbers = []

for i in range(5):
    number = int(input(f'Digite o valor {i+1}: '))
    
    if i == 0 or number > numbers[-1]:
        numbers.append(number)
        print('Valor inserido no fim da lista')
        
    else:
        pos = 0
        while pos < len(numbers):
            if number <= numbers[pos]:
                numbers.insert(pos, number)
                print(f'valor inserido na posição {pos} da lista.')
                break
            pos+=1
            
print(f'A lista ordenada ficou assim: {numbers}')