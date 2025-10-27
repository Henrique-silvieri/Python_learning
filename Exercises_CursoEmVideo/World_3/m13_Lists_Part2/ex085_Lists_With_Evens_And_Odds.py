# Create a program where the user can enter seven numerical values and register them in a single list that keeps the even and odd values 
# separated. In the end, display the even and odd values in ascending order.

odd_numbers = []
even_numbers = []
numbers = [odd_numbers, even_numbers]

for i in range(7):
    number = int(input('Digite um número: '))
    
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    
odd_numbers.sort()
even_numbers.sort()

print(f'Os números ímpares digitados foram {numbers[0]}.')
print(f'Os números pares digitados foram {numbers[1]}.')
