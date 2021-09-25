# This Python file uses the following encoding: utf-8
import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:
    
    # Create
    def __init__(self):
        
        self.width = 800
        self.height = 800
        self.white_colour = (255,255,255) # value en rgb
        # on garde la window hors du loop afin de ne pas en générer indéfiniment
        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock() # on crée une instance de Clock du module pygame.time
        
        self.background = GameObject(0,0, self.width, self.height, "Crossy_Rpg_Game/assets/background.png")
        
        self.treasure = GameObject(375, 50, 50,50, "Crossy_Rpg_Game/assets/treasure.png")
        
        self.player = Player(375, 700, 50, 50, "Crossy_Rpg_Game/assets/player.png", 10) # maybe add a random player speed ?
        
        # Let's create Enemies 
        self.enemies = [
            Enemy(0,600, 50, 50, "Crossy_Rpg_Game/assets/enemy.png", 3),
            Enemy(750,400, 50, 50, "Crossy_Rpg_Game/assets/enemy.png", 5),
            Enemy(0,200, 50, 50, "Crossy_Rpg_Game/assets/enemy.png", 7),
        ]
        
       
        
    # Display
        
    def draw_objects(self):
        # on veut remplir la window de blanc tant que le joeur quitte pas
        self.game_window.fill((self.white_colour))
        # on affiche l'image de fond grace à la fonction blit
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y ))
        
    
        pygame.display.update() 
    
    def move_objects (self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies: 
            enemy.move(self.width) # Enemy movement will be constant 
        
    
    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                return True
            if self.detect_collision(self.player, self.treasure):
                return True
            return False
    
    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        
        return True    
        
    # Moove        
    # Game loop`
    def run_game_loop(self): # avec une fonction on break tout le flow !
        player_direction = 0
        
        while True:
        
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # move player up 
                        player_direction = -1 #800 is bottom 0 is top so we need to decrease to go  up
                    elif event.key == pygame.K_DOWN:
                        # move player down
                        player_direction = 1 # We count backward remember !!!
            # Execute logic
            self.move_objects(player_direction)
            # Update display
            self.draw_objects()
            
            # Detect collisions
            if self.check_if_collided():
                return
            
            
            self.clock.tick(60) # on update 60 fois par seconde

    # /Game loop