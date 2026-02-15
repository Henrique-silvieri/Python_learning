# Create a program that has a function called counter(), which receives three parameters: first term, last term and common difference.
# Your program must perform three counts using the created function:
# A) From 1 to 10, counting by 1
# B) From 10 to 0, counting by 2
# C) A custom count defined by the user

from time import sleep

def counter(firstTerm, lastTerm, commonDifference):
    if commonDifference < 0:
        commonDifference *= -1
    
    print(f'Contagem de {firstTerm} até {lastTerm} de {commonDifference} em {commonDifference}.')
    sleep(2)
    
    count = firstTerm
    if firstTerm < lastTerm:
        while count <= lastTerm:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += commonDifference
    else:
        while count >= lastTerm:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count -= commonDifference
    print('Fim.')


counter(1, 10, 1)
print('='*30)
counter(10, 0, 2)
print('='*30)
print('Agora é sua vez de fazer o contador')
ft = int(input('Digite o inicio da contagem: '))
lt = int(input('Digite o fim da contagem: '))
cd = int(input('Digite o passo da contagem: '))
while cd == 0:
    print('ERRO! A contagem não pode ter passo = 0')
    cd = int(input('Digite o passo da contagem: '))
counter(ft, lt, cd)
