import pygame
from .case import *
from constante import *

class Riviere(Case):
    
    def __init__(self, x, y):
        
        image = "img/Riviere.png"
        
        super().__init__(x, y, image)
        
        self.is_accessible = True