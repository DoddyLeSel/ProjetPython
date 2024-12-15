import pygame
from .case import *
from constante import *
from game import *
class Fumee(Case):
    
    def __init__(self,x,y,duree):
        
        image="img/fumé.png"
        super().__init__(x, y, image)
        self.accessible= True
        self.duree=duree #duré pour laquelle, la fumé est active
        self.est_active=True
        self.is_accessible = True  # definir l'accessibilité pour les unités
        
    def temps_restant(self):
        
       # Diminue la durée de la fumée. Désactive la fumée lorsqu'elle expire.
        if self.duree>0:
            self.duree-=1
        if self.duree==0:
            
            self.est_active=False
            
    def draw_case(self, game):

    #Dessine la case de fumée à l'écran en utilisant son image.

        image = pygame.image.load(self.image).convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        game.screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))  

    
    
