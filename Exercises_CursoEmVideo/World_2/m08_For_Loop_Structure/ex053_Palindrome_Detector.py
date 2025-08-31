# Write a program that reads any phrase and determines whether or not it is a palindrome, disregarding spaces.

phrase = input('digite uma frase: ')
processedPhrase = phrase.replace(' ', '').lower()
inveredPhrase = processedPhrase[::-1]

if processedPhrase == inveredPhrase:
    print(f'A frase {phrase} é um palíndromo')
else:
    print(f'A frase {phrase} não é um palíndromo')
