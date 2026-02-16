# Create a mini-system that utilizes Python's Interactive Help. The user will type the command and the manual will appear. 
# When the user types the word 'FIM' (END), the program will close."
# NOTE: use colors.

from time import sleep
from pydoc import render_doc

colors = (
    '\033[m',            # 0 - without color
    '\033[0;30;41m',     # 1 - red color
    '\033[0;30;42m',     # 2 - green color
    '\033[0;30;43m',     # 3 - yellow color
    '\033[0;30;44m',     # 4 - blue color
    '\033[0;30;45m',     # 5 - purple color
    '\033[0;30;107m'     # 6 - white color
)



def hlp(command):
    title(f'ACESSANDO AS INFORMAÇÕES DO COMANDO "{command}"', 4)
    print(colors[6], end='')
    print(render_doc(command, "Help on %s"))
    print(colors[0], end='')


def title(text, color=0):
    lenText = len(text) + 4
    print(colors[color], end='')
    print('~'*lenText)
    print(f'  {text}  ')
    print('~'*lenText)
    print(colors[0], end='')
    print('')

com = ''
while True:
    title('SISTEMA DE AJUDA PyHELP', 5)
    com = str(input('Digite a função ou biblioteca deseja ver mais informações >>> '))
    if com.upper() == 'FIM':
        break
    else:
        hlp(com)
    sleep(1)

title('ATÉ LOGO!', 1)