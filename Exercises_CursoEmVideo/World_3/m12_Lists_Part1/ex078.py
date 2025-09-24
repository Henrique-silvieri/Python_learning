# Write a program that reads 5 numerical values and stores them in a list.
# At the end, display which was the largest and the smallest value entered and their respective positions in the list.

values = []

for i in range(0,5):
    values.append(int(input('Digite um número: ')))

print(f'A lista tem os seguintes valores {values}.')
print(f'O maior número da lista é {max(values)}.')
print(f'O menor número da lista é {min(values)}.')