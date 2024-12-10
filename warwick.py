import pygame

from unit import *

class Warwick(Unit):
    """
    Construit l'unité Warwick

    Paramètres
    ----------
    x, y : Positions initiales du personnage
        
    team : 'player_1' ou 'player_2', défini l'équipe de l'unité.
    """
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 4
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen, ENTREE): 
        
        #Affiche l'unité sur l'écran
    
        #Affiche les rectangles de déplacement
        self.draw_PM(screen, ENTREE)
        
        #Affiche l'image de l'unité
        image = pygame.image.load("img/Warwick.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
        
        #Affiche la barre de santé
        self.draw_health_bar(screen)

    def skill_1(self, game):
        
        #Compétence : Morsure, attaque à 1 case de distance et rend de la vie
        
        #######################################
        #Défini les paramètres de la compétence
        nom = "Morsure"
        portee = 1
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            positions += [(self.x + i, self.y),
                         (self.x, self.y + i)]
        heal = 10
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y, positions)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in list_cursor and unit.team != self.team :
                unit.health -= self.attack_power
                self.health += heal
                
                if self.health > self.max_health :
                    self.health = self.max_health

        