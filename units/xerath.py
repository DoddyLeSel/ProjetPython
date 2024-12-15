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
        
        NOM = "Xerath"             #Nom de l'unité
        VIE = 1                    #Vie actuelle
        VIE_MAX = 100              #Stat de vie maximale
        DAMAGE = 20                #Stat d'attaque           
        PM = 2                     #Point de mouvement
        image = "img/Xerath.png"   #Lien du sprite de l'unité
        
        super().__init__(x, y, NOM, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        
        self.skill_1_nom = "Rayon Arcanique"           #Nom du sort 1
        self.skill_1_img = "img/XerathA.png"           #Lien de l'icone du sort 1
        
        self.skill_2_nom = "Oeil de la Destruction"    #Nom du sort 2
        self.skill_2_img = "img/XerathZ.png"           #Lien de l'icone du sort 2
        
        self.skill_3_nom = "Orbe d'Électrocution"      #Nom du sort 3
        self.skill_3_img = "img/XerathE.png"           #Lien de l'icone du sort 3


    def skill_1(self, game):
        
        #Compétence : Rayon Arcanique, lance un rayon qui fait des dégâts sur plusieurs cases en ligne
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 20 + 0.1 * self.attack_power
        portee = 5
        positions = [(self.x, self.y)]                                                          #Positions que peut prendre le sort
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) == abs(i) or abs(j) + abs(i) == abs(j) and (i,j) != (0,0):   #Conditions pour former une croix
                    positions += [(self.x + i, self.y + j)]
        
        zone = "xerath_skill_1"                                                                 #Ce sort défini une zone spéciale définie dans le fichier cursor
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions, zone=zone)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)         #Applique les dégats


    def skill_2(self, game):
        
        #Compétence : Oeil de la Destruction, attaque à 5 de distance sur une petite zone
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 20 + 0.1 * self.attack_power
        portee = 5
        positions = [(self.x, self.y)]                                      #Positions que peut prendre le sort
        for i in range(-portee,portee +1):                        
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) <= portee and (i,j) != (0,0):            #Conditions pour former un losange
                    positions += [(self.x + i, self.y + j)]
        
        aoe = 1                    
        zone = []                                                             #Attaque dans une zone en forme de croix
        for k in range(-aoe, aoe+1):
            for l in range(-aoe, aoe+1):
                if abs(k) + abs(l) <= aoe:
                    zone += [(k,l)]
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions, zone=zone)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)                    #Applique les dégats
        
    def skill_3(self, game):
        
        #Compétence : Orbe d'Électrocution, étourdi un ennemi
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 5 + 0.1 * self.attack_power
        portee = 4
        positions = [(self.x, self.y)]                                                              #Positions que peut prendre le sort
        for i in range(-portee,portee +1):
            for j in range(-portee,portee +1):
                if abs(j) + abs(i) == abs(i) or abs(j) + abs(i) == abs(j) and (i,j) != (0,0):       #Conditions pour former une croix
                    positions += [(self.x + i, self.y + j)]
        
        #######################################
        
        #Appelle un curseur pour définir l'endroit où utiliser la compétence
        cursor = Cursor(self.x, self.y,positions)
        list_cursor = cursor.move_cursor(game)
        
        #Applique les effets de la compétence
        self.calcul_damage(game, list_cursor, puissance)                       #Applique les dégats
        self.stun(game, list_cursor)                                           #Applique le stun