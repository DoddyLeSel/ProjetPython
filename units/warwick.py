import pygame

from units import *

class Warwick(Unit):
    """
    Construit l'unité Warwick

    Paramètres
    ----------
    x, y : Positions initiales du personnage
        
    team : 'player_1' ou 'player_2', défini l'équipe de l'unité.
    """
    def __init__(self, x, y, team):
        
        NOM = "Warwick"
        VIE = 100
        DAMAGE = 20
        VIE_MAX = 100
        PM = 4
        image = "img/Warwick.png"
        
        super().__init__(x, y, NOM, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        
        self.skill_1_nom = "Dents de la Bête"
        self.skill_1_img = "img/WarwickA.png"
        
        self.skill_2_nom = "Traque Sanguinaire"
        self.skill_2_img = "img/WarwickZ.png"
        
        self.skill_3_nom = "Hurlement Bestial"
        self.skill_3_img = "img/WarwickE.png"
        
        
    def skill_1(self, game):
        
        #Compétence : Dents de la Bête, attaque à 1 case de distance et rend de la vie
        
        #######################################
        #Défini les paramètres de la compétence
        puissance = 20 + 0.5 * self.attack_power
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
        hit = self.calcul_damage(game, list_cursor, puissance)
        
        if hit :
            self.heal(game, heal)


    def skill_2(self, game):
        
        #Compétence : Traque Sanguinaire, augmente ses PM de 3 points et double sa stat d'attaque
        
        #######################################
        #Défini les paramètres de la compétence
        boost_PM = 3
        boost_attack = self.attack_power
        #######################################
        
        
        #Applique les effets de la compétence
        self.PM += boost_PM
        self.attack_power += boost_attack
        
        self.own_boost_PM = True
        self.own_boost_attack = True
        
    def skill_3(self, game):
        
        #Compétence : Hurlement Bestial, étourdi les ennemis à 1 case de distance autour de lui
        
        #######################################
        #Défini les paramètres de la compétence
        portee = 1
        positions = [(self.x, self.y)]
        for i in range(-portee,portee +1):
            positions += [(self.x + i, self.y),
                         (self.x, self.y + i)]
        #######################################

        #Applique les effets de la compétence
        self.stun(game, positions)