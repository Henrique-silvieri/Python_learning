# Create a program that reads multiple integer numbers from the keyboard. The program should only stop when the user enters the value 999, which is the stop condition. At the end, display how many numbers were entered and what their sum was (disregarding the flag).

total = number = count = 0

print('-Programa de soma-\n')
while True:
    number = int(input('Digite um número para adicionar a soma (ou digite "999" para sair): '))
    total += number
    count += 1
    if number == 999:
        break

print(f'Foram digitados {count} números, e o valor da soma dos números digitados é {total}.')