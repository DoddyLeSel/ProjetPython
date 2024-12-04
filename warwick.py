import pygame

from unit import *

class Warwick(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        
        image = pygame.image.load("Warwick.png").convert_alpha()
        image = pygame.transform.scale(image,(CELL_SIZE, CELL_SIZE))
        
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(image,(self.x * CELL_SIZE, self.y * CELL_SIZE))

    def skill_1(self,screen):
        #Compétence : Morsure, attaque à 1 case de distance et rend de la vie
        nom = "Morsure"
        portee = 1
        positions = []
        for i in range(1,portee +1):
            positions += [(self.x + i, self.y),
                         (self.x - i, self.y),
                         (self.x, self.y + i),
                         (self.x, self.y - i)]
            
        self.afficher_position(screen,positions, BLUE)
        
        cursor=Cursor(self.x, self.y,RED)
        cursor.move_cursor(screen)
        