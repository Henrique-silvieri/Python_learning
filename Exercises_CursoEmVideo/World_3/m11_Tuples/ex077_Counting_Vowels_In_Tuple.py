# Create a program that contains a tuple with several words (do not use accents). After that, for each word, display which vowels it contains.

words = (
    'cachorro',
    'computador',
    'banana',
    'janela',
    'livro',
    'telefone',
    'papel',
    'copo',
    'carro',
    'porta'
)

vowels = 'aeiou'

for word in words:
    print(f'Na palavra {word} temos as vogais: ', end='')
    
    for v in vowels:
        if v in word:
            print(v, end=' ')
    print('\n')