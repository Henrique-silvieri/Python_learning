# Create a program that reads multiple integer numbers from the keyboard. The program should only stop when the user enters the value 999, which is the stop condition. At the end, display how many numbers were entered and what their sum was (disregarding the flag).

flag = 999
sum = 0
number = 0

print('-Programa de soma-\n')
while number != flag:
    number = int(input('Digite um número para adiionar a soma (ou digite "999" para sair): '))
    if number != flag:
        sum += number
    else:
        break

print(f'O valor da soma dos números digitados é {sum}.')