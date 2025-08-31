# Create a program that displays a countdown on the screen for the fireworks explosion, counting from 10 to 0, with a 1-second pause between each number.

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1) #second
print('A bomba explodiu!!')
