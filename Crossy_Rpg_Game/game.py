# This Python file uses the following encoding: utf-8
import pygame
from gameObject import GameObject


class Game:
    
    def __init__(self):
        # C'est mieux de définir notre tuple pour la taille grâce à des variables
        # Plutot que de hardcoder comme un porc
        # avec .self ca devient une propriété propre à un objet de la classe Game
        self.width = 800
        self.height = 800
        self.white_colour = (255,255,255) # value en rgb
        # on garde la window hors du loop afin de ne pas en générer indéfiniment
        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock() # on crée une instance de Clock du module pygame.time
        
        self.background = GameObject(0,0, self.width, self.height, "Crossy_Rpg_Game/assets/background.png")
        # background_image = pygame.image.load("Crossy_Rpg_Game/assets/background.png") 
        # # pb de chemin /Users/macuser/Documents/PYTHON-OLIVIER/learning-python/Pygame_Rpg/Crossy_Rpg_Game/main.py
        # # ne fonctionne pas dans le shell avec Pygame_Rpg/Crossy_Rpg_Game/assets/background.png
        # self.background = pygame.transform.scale(background_image,(self.width,self.height))
        self.treasure = GameObject(375, 50, self.width, self.height, "Crossy_Rpg_Game/assets/treasure.png")
        treasure_image = pygame.image.load("Crossy_Rpg_Game/assets/treasure.png")
        
        self.treasure = pygame.transform.scale(treasure_image, (50, 50))
        
    def draw_objects(self):
        # on veut remplir la window de blanc tant que le joeur quitte pas
        self.game_window.fill((self.white_colour))
        # on affiche l'image de fond grace à la fonction blit
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        # on blit avant de tout rafraichir
        # on affiche le trésor
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
    
        pygame.display.update() 
            
    # Game loop
    def run_game_loop(self): # avec une fonction on break tout le flow !
        while True:
        
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            # Execute logic
            # Update display
            self.draw_objects()
            self.clock.tick(60) # on update 60 fois par seconde

    # /Game loop