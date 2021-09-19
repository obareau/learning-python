
import pygame

pygame.init()

# Game code
# on crée la fenétre de jeu
# C'est mieux de définir notre tuple pour la taille grâce à des variables
width = 800
height = 800
white_colour = (255,255,255) # value en rgb
# on garde la window hors du loop afin de ne pas en générer indéfiniment
game_window = pygame.display.set_mode((width,height))

clock = pygame.time.Clock() # on crée une instance de Clock du module pygame.time
# Game loop
def run_game_loop(): # avec une fonction on break tout le flow !
    while True:
        # on veut remplir la window de blanc tant que le joeur quitte pas
        game_window.fill((white_colour))
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
