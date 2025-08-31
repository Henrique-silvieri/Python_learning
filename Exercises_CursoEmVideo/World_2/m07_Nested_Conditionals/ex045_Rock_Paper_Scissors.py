# Create a program that makes the computer play Rock, Paper, Scissors with you.

import random

userNumber = int (input('qual voce escolhe? \n1 - pedra \n2 - papel \n3 - tesoura \n\n'))
botNumber = random.randint(1,3)

# user choice rock
if userNumber == 1 and botNumber == 1:
    print('Eu tambem escolhi pedra, empatamos!')
elif userNumber == 1 and botNumber == 2:
    print('Eu escolhi papel, eu ganhei2!')
elif userNumber == 1 and botNumber == 3:
    print('Eu escolhi tesoura, você ganhou!')

# user choice paper
elif userNumber == 2 and botNumber == 2:
    print('Eu tambem escolhi papel, empatamos!')
elif userNumber == 2 and botNumber == 1:
    print('Eu escolhi pedra, você ganhou!')
elif userNumber == 2 and botNumber == 3:
    print('Eu escolhi tesoura, eu ganhei!')

# user choice scissors
elif userNumber == 3 and botNumber == 3:
    print('Eu tambem escolhi tesoura, empatamos!')
elif userNumber == 3 and botNumber == 1:
    print('Eu escolhi pedra, eu ganhei!')
elif userNumber == 3 and botNumber == 2:
    print('Eu escolhi papel, voce ganhou!')
