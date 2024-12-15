import pygame


from .case import *
from constante import *

class Trap(case):
    
    def __init__(self,x,y):
        
        image="img/Baron_Nashor.png" 
        super().__init__(x, y, image)
        
        self.is_accessible = True


   