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

        self.x = x
        self.y = y
        self.x_origin = x
        self.y_origin = y
        
        self.color = color
        self.color2 = color2
        self.positions = positions
        self.zone = zone
        
    def move_cursor(self, game):
    
        #Déplace le curseur à l'aide des événements pygame et renvoi la liste des positions finales du curseur
       
        self.draw_cursor(game)
        
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
                        
                    self.draw_cursor(game)
                
                    if event.key == pygame.K_RETURN:
                        l=[]
                        for pos in self.zone :
                            l += [(self.x + pos[0], self.y + pos[1])]
                        return l
                    
                    
    def draw_cursor(self, game):
        
        #Affiche le curseur
        
        game.grid_flip_display()
        
        self.afficher_position(game.screen)
        
        for pos in self.zone :
            if 0 <= (self.x+pos[0]) < GRID_SIZE and 0 <= (self.y+pos[1]) < GRID_SIZE :
                pygame.draw.rect(game.screen, self.color, ((self.x+pos[0])*CELL_SIZE, (self.y+pos[1])*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(game.screen, WHITE,((self.x+pos[0])*CELL_SIZE, (self.y+pos[1])*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            
        game.unit_flip_display()
        
        pygame.display.flip()
        

    def afficher_position(self, screen):
        
        #Affiche les positions possibles pour la compétence
        
        for pos in self.positions :
            if pos != (self.x_origin, self.y_origin) and 0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE:
                pygame.draw.rect(screen, self.color2, (pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, WHITE,(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)