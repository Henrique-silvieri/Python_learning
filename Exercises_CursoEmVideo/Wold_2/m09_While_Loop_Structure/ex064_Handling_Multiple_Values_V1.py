# Create a program that reads multiple integer numbers from the keyboard. The program should only stop when the user enters the value 999, which is the stop condition. At the end, display how many numbers were entered and what their sum was (disregarding the flag).

flag = 999
total = 0
number = 0
count = 0

print('-Programa de soma-\n')
while number != flag:
    number = int(input('Digite um número para adicionar a soma (ou digite "999" para sair): '))
    if number != flag:
        total += number
    else:
        break
    count += 1

print(f'Foram digitados {count} números, e o valor da soma dos números digitados é {total}.')