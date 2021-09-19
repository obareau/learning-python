# This Python file uses the following encoding: utf-8
import pygame

pygame.init()

# Game code
# on creé la fenétre de jeu
# C'est mieux de définir notre tuple pour la taille grâce à des variables
# Plutoit que de hardcoder comme un porc
width = 800
height = 800
white_colour = (255,255,255) # value en rgb
# on garde la window hors du loop afin de ne pas en générer indéfiniment
game_window = pygame.display.set_mode((width,height))

clock = pygame.time.Clock() # on crée une instance de Clock du module pygame.time

background_image = pygame.image.load("assets/background.png") 
# pb de chemin /Users/macuser/Documents/PYTHON-OLIVIER/learning-python/Pygame_Rpg/Crossy_Rpg_Game/main.py
# ne fonctionne pas dans le shell avec Pygame_Rpg/Crossy_Rpg_Game/assets/background.png
background = pygame.transform.scale(background_image,(width,height))

treasure_image = pygame.image.load("assets/treasure.png")
treasure = pygame.transform.scale(treasure_image, (50, 50))
# Game loop
def run_game_loop(): # avec une fonction on break tout le flow !
    while True:
        # on veut remplir la window de blanc tant que le joeur quitte pas
        game_window.fill((white_colour))
        # on affiche l'image de fond grace à la fonction blit
        game_window.blit(background, (0,0)) # le tuple (x,y) = (0,0)= top left corner
        # on blit avant de tout rafraichir
        # on affiche le trésor
        game_window.blit(treasure, (375, 50))
        pygame.display.update()  
        
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        # Execute logic
        # Update display

        clock.tick(60) # on update 60 fois par seconde

# /Game loop

run_game_loop()

pygame.quit()
quit()
