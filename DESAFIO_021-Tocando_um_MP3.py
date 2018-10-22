print('=====================DESAFIO_021=====================')
print('''Faça um programa em python que abra e reproduza 
um áudio de um arquivo MP3\n''')
print ('=====================PROGRAMA======================')
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input('Tocando a musica')




