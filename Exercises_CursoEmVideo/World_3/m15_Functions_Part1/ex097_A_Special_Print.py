# Create a program that has a function called write(), which recives a any text as a parameter and display a message with adaptable size.
# Ex:
# write('Hello, World!')
# Output:
# ~~~~~~~~~~~~~~~~~
#   Hello, World!
# ~~~~~~~~~~~~~~~~~

def write(text):
    lenText = len(text) + 4
    print('~'*lenText)
    print(f'  {text}')
    print('~'*lenText)


text = input('Digite algo: ')
write(text)