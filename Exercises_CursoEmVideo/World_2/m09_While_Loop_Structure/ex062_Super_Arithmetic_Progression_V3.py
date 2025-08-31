# Improve ex061 by asking the user if they want to display additional terms. 
# The program ends when the user indicates that they want to display 0 terms.

firstTerm = int(input('Digite o primeiro termo de uma progressão aritmética (P.A): '))
commonDifference = int(input('Digite a razão da progressão aritmética: '))

term = firstTerm
count = 1
totalTerms = 10
moreTerms = 10

while moreTerms != 0:
    firstInThisRound = True
    while count <= totalTerms:
        if firstInThisRound:  
            print(term, end=' ')
            firstInThisRound = False
        else:
            print(f'- {term}', end=' ')
        term += commonDifference
        count += 1
    moreTerms = int(input('Deseja mostrar mais quantos termos? '))
    totalTerms += moreTerms

print('Fim do programa.')

