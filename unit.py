import pygame
import random
from constante import *
from abc import ABC, abstractmethod
from cursor import *

class Unit(ABC):
    """
    Classe abstraite pour représenter une unité.

    ...
    Attributs
    ---------
    x : int
        La position x de l'unité sur la grille.
    y : int
        La position y de l'unité sur la grille.
    health : int
        La santé de l'unité.
    max_health : int
        La santé maximale de l'unité
    attack_power : int
        La puissance d'attaque de l'unité.
    team : str
        L'équipe de l'unité ('player' ou 'enemy').
    is_selected : bool
        Si l'unité est sélectionnée ou non.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, max_health, attack_power, PM, image, team):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque et une équipe.

        Paramètres
        ----------
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        health : int
            La santé de l'unité.
        attack_power : int
            La puissance d'attaque de l'unité.
        team : str
            L'équipe de l'unité ('player' ou 'enemy').
        """
        self.x = x
        self.y = y
        
        self.x_PM = self.x   #coord des rectangles de selection
        self.y_PM = self.y
        
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.PM = PM
        self.image = image
        self.team = team  # 'player_1' ou 'player_2'
        self.is_selected = False
        self.skill_used = False
        self.returnn = False
        self.mouvement = False
        
        
    def move_PM(self, dx, dy):
        """Déplace le carre de selection de dx, dy."""
        if self.x - self.PM <= self.x_PM + dx <= self.x + self.PM and self.y - self.PM <= self.y_PM + dy <= self.y + self.PM and 0 <= self.x_PM + dx < GRID_SIZE and 0 <= self.y_PM + dy < GRID_SIZE and self.returnn ==False:
        # on compare avec self.x - pm cad par rapport a la position du perso 
            
            #pour former le losange
            if self.x_PM + dx == self.x or self.y_PM +dy == self.y:    
                self.x_PM += dx
                self.y_PM += dy
    
    
    def move(self):
        if 0 <= self.x_PM< GRID_SIZE and 0 <= self.y_PM < GRID_SIZE:
            self.x = self.x_PM   #la derniere coord du rect jaune
            self.y = self.y_PM
            

    def draw_PM (self, screen) : 
        #dessiner les rect LIGHT_YELLOW (zone de mouvement possible)
        
        if self.is_selected and self.returnn ==False : 
            for i in range(self.x - self.PM, self.x + self.PM + 1):
                for j in range(self.y - self.PM, self.y + self.PM + 1):
                    # Vérifiez que les coordonnées sont valides dans la grille
                    if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and (i,j) != (self.x,self.y):
                        #pour former un lesange 
                        if i == self.x or j == self.y:
                            pygame.draw.rect(screen, LIGHT_YELLOW, (i * CELL_SIZE  , j * CELL_SIZE , CELL_SIZE -1 , CELL_SIZE -1)) #-1 pour garder les bordures blanches
        
            #dessiner le rect YELLOW (position actuelle)
            pygame.draw.rect(screen, YELLOW, (self.x_PM * CELL_SIZE, self.y_PM * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        
    def draw(self, screen):
        
        #Affiche l'unité sur l'écran
    
        #Affiche les rectangles de déplacement
        if self.mouvement ==True :
            
            self.draw_PM(screen)
        
        #Affiche l'image de l'unité
        image = pygame.image.load(self.image).convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))
        
        #Affiche la barre de santé
        self.draw_health_bar(screen)


    def draw_health_bar(self, screen):
        # dimensions 
        bar_width = CELL_SIZE #largeur
        bar_height = 5        #hauteur
        x = self.x * CELL_SIZE
        y = self.y * CELL_SIZE - bar_height - 2  # position de la barre (au-dessus du personnage)
        
        #Calcul de la largeur de la barre verte
        actual_health = self.health / self.max_health
        green_width = int(bar_width * actual_health)
        
        #Dessine la barre rouge 
        pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
        #Dessine la barre verte
        pygame.draw.rect(screen, GREEN, (x, y, green_width, bar_height))
        
        
    def skill_1(self):
        pass
    
    def calcul_damage(self, game, zone_degats, puissance):
        
        hit = False
        
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in zone_degats and unit.team != self.team :
                unit.health -= puissance
                hit = True
                
        return True