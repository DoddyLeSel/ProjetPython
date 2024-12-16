import pygame
import random

from constante import *
from abc import ABC, abstractmethod
from cursor import *
from board import *

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
    name : str
        Nom de l'unité
    health : int
        La santé de l'unité.
    max_health : int
        La santé maximale de l'unité
    attack_power : int
        La puissance d'attaque de l'unité.
    PM : int
        Point de mouvement de l'unité
    image : str
        Lien du sprite représentant l'unité
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
    draw(screen, grille, pos_unit)
        Dessine l'unité sur la grille.
    draw_health_bar(screen)
        Dessine la barre de vie des personnages
    calcul_damage(game, zone_degats, puissance)
        Calcule les dégats pris par une ou plusieurs unités
    slow(game, zone_slow, slow)
        Ralenti les unités dans la zone de ralentissement
    stun(game, zone_stun)
        Etourdi les ennemis dans la zone d'étourdissement
    heal(game, heal)
        Soigne l'unité
    fin_boost(self)
        Met fin au boosts de l'unité au tour suivant
    skill_1()
        Lance le sort 1
    skill_2()
        Lance le sort 2
    skill_3()
        Lance le sort 3
    """

    def __init__(self, x, y, name, health, max_health, attack_power, PM, image, team):
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
        
        self.name = name
        
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.attack_power_origin = attack_power
        self.PM = PM
        self.PM_origin = PM
        self.image = image
        self.team = team  # 'player_1' ou 'player_2'
        
        self.is_selected = False
        self.skill_used = False
        self.returnn = False
        self.mouvement = False
        self.stunt = False
        self.has_item = False #Savoir si le perso a collecté un objet magique 
        
        self.own_boost_PM = False
        self.own_boost_attack = False
        
        self.passage_riv = False
        self.positions = [] #liste contenant les positions accesibles seulement
        self.pos_riv=[] #liste contenant les positions des cases rivieres


    def move_PM(self, dx, dy):
        """Déplace le carre de selection de dx, dy."""
        if self.x - self.PM <= self.x_PM + dx <= self.x + self.PM and self.y - self.PM <= self.y_PM + dy <= self.y + self.PM and 0 <= self.x_PM + dx < GRID_SIZE and 0 <= self.y_PM + dy < GRID_SIZE and self.returnn ==False:
        # ne pas depasser la zone des PM
             
            #pour former le losange
            #if self.x_PM + dx == self.x or self.y_PM +dy == self.y:
            if (self.x_PM + dx, self.y_PM + dy) in self.positions :
                
                self.x_PM += dx
                self.y_PM += dy

                if (self.x_PM , self.y_PM ) in self.pos_riv : #S'il passe par la riviere le PM diminue de 1
                    self.passage_riv = True

   
    def move(self):

        

        if 0 <= self.x_PM< GRID_SIZE and 0 <= self.y_PM < GRID_SIZE:
            self.x = self.x_PM   #la derniere coord du rect jaune
            self.y = self.y_PM

    
        #reinitialiser les listes des posistions une fois le perso a changé de place
        self.positions = []
        self.pos_riv=[]

        


    def draw_PM (self, screen, grille,pos_unit) : 
        #dessiner les rect LIGHT_YELLOW (zone de mouvement possible)     
       
        if self.is_selected and self.returnn ==False : 
            for i in range(self.x - self.PM, self.x + self.PM + 1):
                for j in range(self.y - self.PM, self.y + self.PM + 1):
                    # Vérifiez que les coordonnées sont valides dans la grille
                    if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE : #and (i,j) != (self.x,self.y):
                        
                        #pour former un losange 
                        if abs(i - self.x) + abs(j - self.y) <= self.PM :

                            #Si les cases sont pas des murs
                            for case in grille : 
                                if case.x==i and case.y==j :

                                    #verifier si la case est accessible et n'est pas occupé par une autre unité
                                    pos_unit_temp = pos_unit.copy() # cree une copie temporaire de self.pos_unit
                                    pos_unit_temp.discard((self.x, self.y)) #supprime l'unite elle meme de la copie temporaire pour éviter qu'il soit vérifié
                                    
                                    if case.is_accessible == True and not((i,j) in pos_unit_temp ):

                                        self.positions.append((i,j)) #rempli la liste des positions des cases accesibles

                                        if case.is_riv == True : #si la case est une riviere
                                            self.pos_riv.append((i,j))
                                                                            
            self.voisins()
            for x,y in self.positions:
                if (x,y) in self.pos_riv : #On dessine les passages par la rivieres avec une autre couleur
                    pygame.draw.rect(screen, AQUA_YELLOW, (x * CELL_SIZE  , y * CELL_SIZE , CELL_SIZE -1 , CELL_SIZE -1)) #-1 pour garder les bordures blanches                                    
                else :
                    pygame.draw.rect(screen, LIGHT_YELLOW, (x * CELL_SIZE  , y * CELL_SIZE , CELL_SIZE -1 , CELL_SIZE -1)) 

                   
            #dessiner le rect YELLOW (position actuelle)
            pygame.draw.rect(screen, YELLOW, (self.x_PM * CELL_SIZE, self.y_PM * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
    def voisins(self):

        for x, y in self.positions:
            # Calculer les voisins possibles
            voisins = [
                (x + 1, y),  # droite
                (x - 1, y),  # gauche
                (x, y + 1),  # bas
                (x, y - 1),  # haut
            ]

            # Vérifier s'il y a un voisin dans la liste
            for pos in voisins:
                if not (pos in self.positions):
                    is_not = False
                else :
                    is_not = True
                    break    
            if is_not == False:
                self.positions.remove((x,y)) #on retire une case si elle n'a aucun voisin accesible
                if (x,y) in self.pos_riv : #on la retire de la liste des cases rivieres aussi 
                    self.pos_riv.remove((x,y)) 


    def draw(self, screen, grille, pos_unit):

        
    #Dessine l'unité uniquement si elle n'est pas recouverte par une fumée.
    
    # Vérifie si une fumée recouvre cette unité
        for case in grille:
            if isinstance(case, Fumee) and case.x == self.x and case.y == self.y:
                return  # Ne pas dessiner l'unité si elle est sous une fumée

    # Affiche les rectangles de déplacement si applicable
        if self.mouvement:
            self.draw_PM(screen, grille, pos_unit)

    # Affiche l'image de l'unité

        
        #Affiche l'unité sur l'écran
    
        #Affiche les rectangles de déplacement
        if self.mouvement == True :
            
            self.draw_PM(screen, grille, pos_unit)
        
        #Affiche l'image de l'unité

        image = pygame.image.load(self.image).convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    # Affiche la barre de santé
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


    def reinitialiser_PM(self):
    
     # Reinitialise les PM au début du tour, sauf si des changements ont été appliqués
  
        if self.passage_riv == True : #Diminue la valeur de PM si il est passé par une riviere                    
            self.PM_origin = self.PM_origin - 1
        self.passage_riv = False


    def calcul_damage(self, game, zone_degats, puissance):
        
        hit = False
        
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in zone_degats and unit.team != self.team :
                unit.health -= puissance
                hit = True
                game.messages.append(unit.name + " a pris " + str(puissance) + " points de dégâts" )
                
        return True


    def stun(self, game, zone_stun):
        
        hit = False
        
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in zone_stun and unit.team != self.team :
                unit.stunt = True
                hit = True
                game.messages.append(unit.name + " s'est fait étourdir")


    def slow(self, game, zone_slow, slow):
        
        hit = False
        
        for unit in game.player_1_units + game.player_2_units :
            
            if (unit.x, unit.y) in zone_slow and unit.team != self.team :
                unit.PM += slow
                hit = True
                game.messages.append(unit.name + " s'est fait ralentir de " + str(abs(slow)) + " PM")


    def heal(self, game, heal):
         
        self.health += heal
        
        game.messages.append(self.name + " s'est soigné de " + str(heal))
        
        if self.health > self.max_health :
                self.health = self.max_health
     
     
    def fin_boost(self) :
        
        if self.own_boost_PM :
            self.own_boost_PM = False
        else:
            self.PM = self.PM_origin
            
        if self.own_boost_attack :
            self.own_boost_attack = False
        else:
            self.attack_power = self.attack_power_origin

    @abstractmethod
    def skill_1(self):
        pass
    
    @abstractmethod
    def skill_2(self):
        pass
    
    @abstractmethod
    def skill_3(self):
        pass