# Create a program that will generate five random numbers and store them in a tuple.
# After that, display the list of the generated numbers and also indicate the smallest and the largest value that are in the tuple.

from random import randint

largest = smallest = count = 0
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores aleatórios são:')
for number in numbers:
    print(f'{number} ', end='')
print(f'\nO maior valor foi {max(numbers)} e o menor valor foi {min(numbers)}.')
