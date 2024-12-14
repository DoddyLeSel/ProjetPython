import pygame

from units import *

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
        image = "img/MissFortune.png"
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        
        self.skill_1_nom = "Doublé"
        self.skill_1_img = "img/MissFortuneA.png"
        
        self.skill_2_nom = "Fanfaronne"
        self.skill_2_img = "img/MissFortuneZ.png"
        
        self.skill_3_nom = "Pluie de Balles"
        self.skill_3_img = "img/MissFortuneE.png"
        
        
    def skill_1(self):
        #Compétence : Doublé, attaque simple à 3 de distance
        
        #######################################
        #Défini les paramètres de la compétence
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
        list_cursor = cursor.move_cursor()
        
        #Applique les effets de la compétence
        self.calcul_damage(list_cursor, puissance)


    def skill_2(self):
        #Compétence : Fanfaronne, double les PM
        
        #######################################
        #Défini les paramètres de la compétence
        boost_PM = self.PM
        #######################################
        
        #Applique les effets de la compétence
        self.PM += boost_PM

        self.own_boost_PM = True

    def skill_3(self):
        #Compétence : Pluie de Balles, attaque en zone à 3 de distance et ralenti les ennemis dans la zone
        
        #######################################
        #Défini les paramètres de la compétence
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
        list_cursor = cursor.move_cursor()
        
        #Applique les effets de la compétence
        self.calcul_damage(list_cursor, puissance)
        self.slow(list_cursor, slow)