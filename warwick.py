import pygame

from unit import *

class Warwick(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        
        super().__init__(x, y, VIE, DAMAGE, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        
        image = pygame.image.load("Warwick.png").convert_alpha()
        image = pygame.transform.scale(image,(CELL_SIZE, CELL_SIZE))
        
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(image,(self.x * CELL_SIZE, self.y * CELL_SIZE))

    def skill_1(self):
        
        range = 1
        positions=[]
        for i in range(range):
            position += [(self.x + i, self.y),
                         (self.x - i, self.y),
                         (self.x, self.y + i),
                         (self.x, self.y - i)]
        
        