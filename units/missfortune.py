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
        
        NOM = "Miss Fortune"               #Nom de l'unité
        VIE = 100                          #Vie actuelle
        VIE_MAX = 100                      #Stat de vie maximale
        DAMAGE = 20                        #Stat d'attaque
        PM = 3                             #Point de mouvement
        image = "img/MissFortune.png"      #Lien du sprite de l'unité
        
        super().__init__(x, y, NOM, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        
        self.skill_1_nom = "Doublé"                      #Nom du sort 1
        self.skill_1_img = "img/MissFortuneA.png"        #Lien de l'icone du sort 1
        
        self.skill_2_nom = "Fanfaronne"                  #Nom du sort 2
        self.skill_2_img = "img/MissFortuneZ.png"        #Lien de l'icone du sort 2
        
        self.skill_3_nom = "Pluie de Balles"             #Nom du sort 3
        self.skill_3_img = "img/MissFortuneE.png"        #Lien de l'icone du sort 3
        
        
    def skill_1(self, game):
        #Compétence : Doublé, attaque simple à 3 de distance
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 30 + 0.1 * self.attack_power
        portee = 3
        positions = [(self.x, self.y)]                                       #Positions que peut prendre le sort
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) <= portee and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y, positions)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)            #Applique les degats


    def skill_2(self, game):
        #Compétence : Fanfaronne, double les PM
        
        #######################################
        #Défini les paramètres de la compétence
        boost_PM = self.PM
        #######################################
        
        #Applique les effets de la compétence
        self.PM += boost_PM                          #Booste les PM

        self.own_boost_PM = True                     #Défini que le boost a eu lieu ce tour

    def skill_3(self, game):
        #Compétence : Pluie de Balles, attaque en zone à 3 de distance et ralenti les ennemis dans la zone
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 10 + 0.1 * self.attack_power
        portee = 3
        positions = [(self.x, self.y)]                                        #Positions que peut prendre le sort
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(i) + abs(j) <= portee and (i,j) != (0,0):
                    positions += [(self.x + i, self.y + j)]
        aoe = 1                    
        zone = []                                                             #Attaque dans une zone en forme de croix
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