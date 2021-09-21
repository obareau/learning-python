# This Python file uses the following encoding: utf-8
import pygame

class GameObject:
    
    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path) # on crée une var locale
        self.image = pygame.transform.scale(image (width,height )) 
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # toutes les instances de GameObject aurons ces 4 properties
        
        