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
        image = "img/Warwick.png"
        
        super().__init__(x, y, VIE, VIE_MAX, DAMAGE, PM, image, team)   #Hérite de la classe Unit
        

    def skill_1(self, game):
        
        #Compétence : Morsure, attaque à 1 case de distance et rend de la vie
        
        #######################################
        #Défini les paramètres de la compétence
        nom = "Morsure"
        puissance = 20 + 0.1 * self.attack_power
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
            self.health += heal
            
            if self.health > self.max_health :
                self.health = self.max_health

        