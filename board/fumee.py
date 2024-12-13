import pygame
from .case import *
from constante import *

class fumee(Case):
    
    def __init__(self,x,y,duree):
        
        image="img/fumé.png"
        super().__init__(x, y, image)
        self.accessible= True
        self.duree=duree #duré pour laquelle, la fumé est active
        self.est_active=True
        
    def temps_restant(self):
        
       # Diminue la durée de la fumée. Désactive la fumée lorsqu'elle expire.
        if self.duree>0:
            self.duree-=1
        if self.duree==0:
            
            self.est_active=False
            
    def draw_case(self, screen):
        #Dessine la fumée sur la case.
        if self.est_active:
            image = pygame.image.load(self.image).convert_alpha()
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
    
    
