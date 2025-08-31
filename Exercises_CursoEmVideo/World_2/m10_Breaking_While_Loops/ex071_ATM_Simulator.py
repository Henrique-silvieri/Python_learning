# # Write a program that simulates the operation of an ATM (Automated Teller Machine).
# At the beginning, ask the user what amount of money they wish to withdraw (an integer number), and the program should inform how many bills of each denomination will be delivered.
# Note: Consider that the ATM has bills of R$50, R$20, R$10, and R$1 available.

bill50 = bill20 = bill10 = bill1 = 0

withdraw = int(input('Digito um valor inteiro a ser sacado: '))

while True:
    if withdraw >= 50:
        withdraw -= 50
        bill50 += 1
    elif withdraw >= 20:
        withdraw -= 20
        bill20 += 1
    elif withdraw >= 10:
        withdraw -= 10
        bill10 += 1
    else:
        withdraw -= 1
        bill1 += 1
    
    if withdraw == 0:
        break

print(f'Foram sacados {bill50} notas de R$50.00, {bill20} notas de R$20.00, {bill10} notas de R$10.00 e {bill1} notas de R$1.00.')