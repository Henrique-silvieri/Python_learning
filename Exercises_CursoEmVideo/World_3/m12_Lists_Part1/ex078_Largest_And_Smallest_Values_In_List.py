# Write a program that reads 5 numerical values and stores them in a list.
# At the end, display which was the largest and the smallest value entered and their respective positions in the list.

values = []

for i in range(0,5):
    values.append(int(input('Digite um número: ')))

largest = max(values)
smallest = min(values)

position_largest = []
for i, v in enumerate(values):
    if v == largest:
        position_largest.append(i)

position_smallest = []
for i, v in enumerate(values):
    if v == smallest:
        position_smallest.append(i)


print(f'A lista tem os seguintes valores {values}.')
print(f'O maior número da lista é {largest}, que está na posição {position_largest}.')
print(f'O menor número da lista é {smallest}, que está na posição {position_smallest}.')
