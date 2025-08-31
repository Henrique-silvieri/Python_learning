# Develop a program that reads six integer numbers and display the sum of only those that are even. If the entered value is odd, ignore it.

total = 0

for i in range(6):
    
    numbers = int(input('digite um número inteiro: '))
    if numbers % 2 == 0:
        total = total + numbers 
        
print(f'A soma de todos o numeros pares da lista é de {total}.')
