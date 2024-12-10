import pygame

from unit import *

class Xerath(Unit):
    """
    Construit l'unité Xerath

    Paramètres
    ----------
    x, y : Positions initiales du personnage
        
    team : 'player_1' ou 'player_2', défini l'équipe de l'unité.
    """
    def __init__(self, x, y, team):
        
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 3
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, team)   #Hérite de la classe Unit
        
        
    def draw(self, screen, ENTREE):
        
        #Affiche l'unité sur l'écran
        
        #Affiche les rectangles de déplacement
        self.draw_PM(screen, ENTREE)
        
        #Affiche l'image de l'unité
        image = pygame.image.load("img/Xerath.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
        
        #Affiche la barre de santé
        self.draw_health_bar(screen)

    def skill_1(self, game):
        
        #Compétence : , attaque à 5 de distance sur une petite zone
        
        #######################################
        #Défini les paramètres de la compétence
        nom = ""
        portee = 5
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) <= portee and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        
        zone = [(0,0),(0,1),(1,0),(0,-1),(-1,0)]
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions, zone=zone)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in list_cursor and unit.team != self.team :
                unit.health -= self.attack_power