# Create a program that reads multiple integer numbers from the keyboard. At the end of the execution, display the average of all the values, as well as the largest and the smallest values entered. The program must ask the user whether they want to continue entering values or not

number = total = count = average = largest = smallest = 0

while True:
    number = int(input('Digite um número para calcular a média: '))
    total += number
    count += 1
    
    if count == 1: 
        smallest = largest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    
    continueAnswer = input('Deseja adicionar outro valor (S/N)? ').strip().lower()
    
    if continueAnswer != 's':
        break

average = total/count

print(f'A média dos números digitados é {average}, sendo o maior valor {largest} e o menor valor {smallest}. ')