import pygame
import random
from constante import *

class Trap:
    def __init__(self, nb_traps):
        
        self.nb_traps = nb_traps
        #self.positions = self.gen_trap()
    
    def __init__(self, nb_traps):
        self.nb_traps = nb_traps
        self.positions = set()
    
    def genrer(self):    
        while len(self.positions) < self.nb_traps:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            self.positions.add((x, y))


    def draw_trap(self, screen):
        
        for  x, y in self.positions:
            # Affiche une image ou un rectangle pour représenter le piège
            image = pygame.image.load("Baron_Nashor.png").convert_alpha()
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            screen.blit(image, (x * CELL_SIZE,y * CELL_SIZE))
        