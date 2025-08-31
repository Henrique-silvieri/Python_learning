# Redo ex051, reading the first term and the common difference of an arithmetic progression (AP), displaying the first 10 terms of the progression using the while loop structure.

firstTerm = int(input('Digite o primeiro termo de uma progressão aritimética (P.A) '))
commonDifference = int(input('Digite a razão da progressão aritimética '))
term = firstTerm
count = 0

while count < 10:
    if count == 0: 
        print(term, end='')
    else: 
        print(f' - {term}', end='')
    
    term += commonDifference
    count += 1
