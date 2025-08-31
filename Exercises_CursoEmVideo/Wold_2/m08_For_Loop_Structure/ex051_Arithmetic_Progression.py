# Develop a program that reads the first term and the common difference of an arithmetic progression (A.P.).
# In the end, display the first 10 terms of this progression.

firstTerm = int(input('Digite o primeiro termo de uma progressão aritimética (P.A) '))
commonDifference = int(input('Digite a razão da progressão aritimética '))
tenthTerm = firstTerm + commonDifference * 10

for i in range(firstTerm, tenthTerm, commonDifference):
    if i == firstTerm: 
        print(i, end='')
    else: 
        print(f' - {i}', end='')
