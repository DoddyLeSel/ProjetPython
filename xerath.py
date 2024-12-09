import pygame

from unit import *

class Xerath(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 3
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen, ENTREE): 
        """Affiche l'unité sur l'écran."""
        
        # afficher les rectangles de selection
        self.draw_PM(screen, ENTREE)
        
        # Afficher l'image de l'unité
        image = pygame.image.load("Xerath.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
        
        self.draw_health_bar(screen)

    def skill_1(self,screen):
        #Compétence :
        nom = ""
        portee = 5
        positions = [(self.x, self.y)]
        for i in range(1,portee +1):
            positions += [(self.x + i, self.y),
                         (self.x - i, self.y),
                         (self.x, self.y + i),
                         (self.x, self.y - i)]
            
        self.afficher_position(screen,positions, BLUE)