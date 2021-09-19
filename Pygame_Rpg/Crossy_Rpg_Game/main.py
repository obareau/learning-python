import pygame

pygame.init()

# Game code
# on crée la fenétre de jeu
# C'est mieux de définir notre tuple pour la taille grâce à des variables
width = 800
height = 800
white_colour = (255,255,255) # value en rgb
game_window = pygame.display.set_mode((width,height))
game_window.fill((white_colour))
pygame.display.update()  

pygame.quit()
quit()
