# Create a program that has a function called largest() that receives several integer parameters.
# Your program must analyze all the values and determine which one is the largest.

from time import sleep

def largest(* num):
    count = largest = 0
    
    print('='*35)
    print('\nValores analisados:')
    for value in num:
        print(f'{value} ', end='', flush=True)
        sleep(0.2)
        if count == 0:
            largest = value
        elif value > largest:
            largest = value
        
        count += 1
    print(f'Foram informados {count} valores.')
    print(f'O maior valor é {largest}.\n')
    

largest(2, 4, 3, 7, 9, 3, 5, 20)
largest(3)
largest()
largest(2, 1)