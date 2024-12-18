import pygame
from constante import *
from abc import ABC, abstractmethod

class Case(ABC):
    
    def __init__(self, x, y, image):
        
        self.x = x
        self.y = y
        self.image = image
        self.accessible = True
        self.is_riv = False
        
        
    def draw_case(self, game) :
        image = pygame.image.load(self.image).convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        game.screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))