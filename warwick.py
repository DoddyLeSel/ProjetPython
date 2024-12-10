import pygame

from unit import *

class Warwick(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 4
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen, ENTREE): 
        """Affiche l'unité sur l'écran."""
    
        # afficher les rectangles de selection
        self.draw_PM(screen, ENTREE)
        
        # Afficher l'image de l'unité
        image = pygame.image.load("img/Warwick.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
        
        self.draw_health_bar(screen) # dessiner la barre de sante

    def skill_1(self, game):
        #Compétence : Morsure, attaque à 1 case de distance et rend de la vie
        nom = "Morsure"
        portee = 1
        positions = [(self.x, self.y)]
        for i in range(1,portee +1):
            positions += [(self.x + i, self.y),
                         (self.x - i, self.y),
                         (self.x, self.y + i),
                         (self.x, self.y - i)]
        heal = 10
        
        cursor = Cursor(self.x, self.y, positions)
        list_cursor = cursor.move_cursor(self.x, self.y, game)
        
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in list_cursor and unit.team != self.team :
                unit.health -= self.attack_power
                self.health += heal
                
                if self.health > self.max_health :
                    self.health = self.max_health

        