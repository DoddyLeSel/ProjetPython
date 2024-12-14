import pygame

from units import *

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
        PM = 2
        image = "img/Xerath.png"
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        
        self.skill_1_nom = "Rayon Arcanique"
        self.skill_1_img = "img/XerathA.png"
        
        self.skill_2_nom = "Oeil de la destruction"
        self.skill_2_img = "img/XerathZ.png"
        
        self.skill_3_nom = "Orbe d'électrocution"
        self.skill_3_img = "img/XerathE.png"


    def skill_1(self, game):
        
        #Compétence : Rayon Arcanique, lance un rayon qui fait des dégâts sur plusieurs cases en ligne
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 20 + 0.1 * self.attack_power
        portee = 5
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) == abs(i) or abs(j) + abs(i) == abs(j) and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        
        zone = "xerath_skill_1"
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions, zone=zone)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)


    def skill_2(self, game):
        
        #Compétence : Oeil de la Destruction, attaque à 5 de distance sur une petite zone
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 20 + 0.1 * self.attack_power
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
        self.calcul_damage(game, list_cursor, puissance)
        
    def skill_3(self, game):
        
        #Compétence : Orbe d'électrocution, étourdi un ennemi
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 5 + 0.1 * self.attack_power
        portee = 4
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) == abs(i) or abs(j) + abs(i) == abs(j) and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)
        self.stun(game, list_cursor)