# Write a program that reads a sentence from the keyboard and shows:
# -> How many times the letter "a" appears.
# -> The position where it first appears.
# -> The position where it last appears.

setence = str(input('Digite uma frase: ')).lower()

print(f'A frase escrita tem {setence.count('a')} letras "a".')
print(f'O primeiro "a" aparece na posição {setence.find('a') + 1}.')
print(f'O último "a" aparece na posição {setence.rfind('a') + 1}.')
