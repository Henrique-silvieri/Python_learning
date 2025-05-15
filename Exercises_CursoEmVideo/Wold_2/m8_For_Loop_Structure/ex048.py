# Create a program that calculates the sum of all odd numbers that are multiples of 3 and are found in the range from 1 to 500.

toral = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        print(i)
        total += i

print(total)
