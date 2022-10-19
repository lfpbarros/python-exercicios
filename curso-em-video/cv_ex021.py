# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

from playsound import playsound
import pygame

playsound('audio/miau.mp3')

# Com a versão 1.3.0 do playsound, o script não funcionou. Ao instalar a versão 1.2.2 foi possível com o pip install playsound==1.2.2

# Foi assim que o professor Guanabara fez:

# pygame.init()
# pygame.mixer.music.load('audio/miau.mp3')
# pygame.mixer.music.play()
# input()
# pygame.event.wait()