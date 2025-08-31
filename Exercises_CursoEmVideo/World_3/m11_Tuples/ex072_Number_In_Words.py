# Create a program that has a tuple completely filled with a number spelled out from zero to twenty.
# Your program should read a number from the keyboard (between 0 and 20) and display it in words.

spelled_numbers = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number <= 20:
        break

print(f'Você digitou o número {spelled_numbers[number]}')