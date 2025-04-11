# Make a program in Python that opens and plays an audio file in MP3 format.

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3') #É Preciso Dar um Jeito, Meu Amigo - Erasmo Carlos
pygame.mixer.music.play()
pygame.event.wait()

input('Digite ENTER para encerrar...')
