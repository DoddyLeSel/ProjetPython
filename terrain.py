import pygame
from case import *
from constante import *

class Terrain(Case) :
    
    def __init__(self, x, y):
        
        image = "img/Terrain.png"
        
        super().__init__(x, y, image)
        
        self.is_accessible = True