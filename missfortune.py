import pygame

from unit import *

class MissFortune(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
            
        image = pygame.image.load("MissFortune.png").convert_alpha()
        image = pygame.transform.scale(image,(CELL_SIZE, CELL_SIZE))
        
        if self.is_selected:
            pygame.draw.rect(screen, YELLOW, (self.x * CELL_SIZE,self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(image,(self.x * CELL_SIZE, self.y * CELL_SIZE))

    def skill_1(self,screen):
        #Compétence : 
        nom = ""
        portee = 3
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) <= 3 and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
            
        self.afficher_position(screen,positions, BLUE)
        
        cursor=Cursor(self.x, self.y,positions)
        cursor.move_cursor(screen, self.x, self.y)