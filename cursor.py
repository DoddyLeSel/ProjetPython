import pygame

from unit import *
from constante import *

class Cursor:
    """
    Construit un curseur

    Paramètres
    ----------
    x, y : Positions initiales du curseur
        
    positions : Liste de tuples (x,y) contenant les positions que peut prendre le curseur
        
    zone : Taille/Forme du curseur
        
    color : Couleur du curseur
        
    color2 : Couleur des positions possibles pour le curseur
    """
    def __init__(self, x, y, positions, zone=[(0,0)], color=RED, color2=BLUE):

        self.x = x                              #Position en x
        self.y = y                              #Position en y
        self.x_origin = x                       #Backup pour la position initiale en x
        self.y_origin = y                       #Backup pour la position initiale en y
        
        self.color = color                      #Couleur du curseur
        self.color2 = color2                    #Couleur de la zone d'action (bleu par défaut)
        self.positions = positions              #Positions que peut prendre le curseur
        self.zone = zone                        #Taille de curseur (1 case par défaut)
        self.zone_special = zone
    def move_cursor(self, game):                #Déplace le curseur à l'aide des événements pygame et renvoi la liste de la ou des positions finales du curseur (selon la taille du curseur)
        
        self.afficher_position(game.screen)
        game.unit_flip_display()
        pygame.display.flip()
        
        while True :
            for event in pygame.event.get():
            
                if event.type == pygame.KEYDOWN:
                       
                    dx,dy = 0,0
                    
                    if event.key == pygame.K_LEFT :
                        dx += -1
                    elif event.key == pygame.K_RIGHT :
                        dx += 1    
                    elif event.key == pygame.K_UP :
                        dy += -1  
                    elif event.key == pygame.K_DOWN :
                        dy += 1
                    
                    if (self.x + dx, self.y + dy) in self.positions and 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE :
                        self.x += dx
                        self.y += dy
                    
                    self.zone_spe()
                    
                    self.draw_cursor(game)
                
                    if event.key == pygame.K_RETURN:
                        l=[]
                        for pos in self.zone :
                            l += [(self.x + pos[0], self.y + pos[1])]
                        return l
                    
                    
    def draw_cursor(self, game):              #Affiche le curseur
        
        game.grille.draw_grille(game.screen)
        
        self.afficher_position(game.screen)
        
        for pos in self.zone :
            if 0 <= (self.x+pos[0]) < GRID_SIZE and 0 <= (self.y+pos[1]) < GRID_SIZE :
                pygame.draw.rect(game.screen, self.color, ((self.x+pos[0])*CELL_SIZE, (self.y+pos[1])*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(game.screen, WHITE,((self.x+pos[0])*CELL_SIZE, (self.y+pos[1])*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            
        game.unit_flip_display()
        
        pygame.display.flip()
        

    def afficher_position(self, screen):           #Affiche la zone d'action du curseur
        
        for pos in self.positions :
            if pos != (self.x_origin, self.y_origin) and 0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE:
                pygame.draw.rect(screen, self.color2, (pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, WHITE,(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)


    def zone_spe(self):
        if self.zone_special == "xerath_skill_1":
            self.zone = []
                        
            if self.x - self.x_origin < 0 :
                pas_x = -1
            else:
                pas_x = 1
                        
            if self.y - self.y_origin < 0 :
                pas_y = -1
            else:
                pas_y = 1
                        
            if self.x - self.x_origin == 0 :
                constante_x = 1
            else :
                constante_x = 0
                        
            if self.y - self.y_origin == 0 :
                constante_y = 1
            else :
                constante_y = 0
                        
            for i in range(0, self.x - self.x_origin + constante_x, pas_x):
                for j in range(0, self.y - self.y_origin + constante_y, pas_y):
                    self.zone += [(-i, -j)]