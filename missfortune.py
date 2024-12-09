import pygame

from unit import *

class MissFortune(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 3
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen, ENTREE): 
        """Affiche l'unité sur l'écran."""
    
        self.draw_PM(screen, ENTREE)
        # Afficher l'image de l'unité
        image = pygame.image.load("MissFortune.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def skill_1(self,screen, l_unit_1, l_unit_2):
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
        (x_cursor,y_cursor)=cursor.move_cursor(screen, self.x, self.y)
        
        for unit in l_unit_1 + l_unit_2 :
            
            if (unit.x, unit.y) == (x_cursor, y_cursor) and unit.team != self.team :
                unit.health -= self.attack_power
