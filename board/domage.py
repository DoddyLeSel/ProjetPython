import pygame
from units import *

from .case import Case
from constante import *

class Domag(Case):
    
    def __init__(self,x,y):
        
        image="img/Baron_Nashor.png" 
        super().__init__(x, y, image)
        
        self.is_accessible = True
        self.damages = 5  # Dégâts infligés par la case Domag

    def infliger_domage(self, unit):
        # Méthode pour infliger des dégâts à une unité
        if unit.x == self.x and unit.y == self.y:
            unit.health -= self.damages
            
            print(f"{unit.name} a pris {self.damages} points de dégâts sur la case Domag.")