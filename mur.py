import pygame
from case import *
from constante import *

class Mur(Case) :
    
    def __init__(self, x, y):
        
        image = "img/Mur.png"
        
        super().__init__(x, y, image)
        
        self.is_accessible = False