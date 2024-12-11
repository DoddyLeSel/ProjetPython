import pygame

from unit import *

class MissFortune(Unit):
    """
    Construit l'unité Miss Fortune

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
        image = "img/MissFortune2.webP"
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        

    def skill_1(self, game):
        #Compétence : Doublé, attaque simple à 3 de distance
        
        #######################################
        #Défini les paramètres de la compétence
        nom = "Doublé"
        puissance = 30 + 0.1 * self.attack_power
        portee = 3
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) <= portee and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y, positions)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)


    def skill_2(self, game):
        #Compétence : Fanfaronne, double les PM
        
        #######################################
        #Défini les paramètres de la compétence
        nom = "Fanfaronne"
        boost_PM = self.PM
        #######################################
        
        #Applique les effets de la compétence
        self.PM += boost_PM

        self.own_boost_PM = True

    def skill_3(self, game):
        #Compétence : Pluie de Balles, attaque en zone à 3 de distance et ralenti les ennemis dans la zone
        
        #######################################
        #Défini les paramètres de la compétence
        nom = "Pluie de Balles"
        puissance = 10 + 0.1 * self.attack_power
        portee = 3
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(i) + abs(j) <= portee and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        aoe = 1                    
        zone = []
        for k in range(-aoe, aoe+1):
            for l in range(-aoe, aoe+1):
                if abs(k) + abs(l) <= aoe:
                    zone += [(k,l)]
                    
        slow = -1
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y, positions, zone=zone)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)
        self.slow(game, list_cursor, slow)