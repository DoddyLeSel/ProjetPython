import pygame
import random

from unit import *
from warwick import *
from xerath import *
from missfortune import *
from cursor import *
from constante import *
from trap import *

class Game:
    """
    Classe pour représenter le jeu.

    ...
    Attributs
    ---------
    screen: pygame.Surface
        La surface de la fenêtre du jeu.
    player_1_units : list[Unit]
        La liste des unités du joueur 1.
    player_2_units : list[Unit]
        La liste des unités du joueur 2.
    """
    ENTREE = 0 #pour effacer les rect de selection une fois on appuie sur entree
    
    def __init__(self, screen):
        """
        Construit le jeu avec la surface de la fenêtre.

        Paramètres
        ----------
        screen : pygame.Surface
            La surface de la fenêtre du jeu.
        """
        self.screen = screen
        self.player_1_units = [Warwick(6, 1, 'player_1'), Xerath(7,1, 'player_1'), MissFortune(8,1, 'player_1')]

        self.player_2_units = [Warwick(6, 13, 'player_2'), Xerath(7,13, 'player_2'), MissFortune(8,13, 'player_2')]
        
        self.trap = Trap(5)
        self.trap.genrer() #genrer les positions des pieges pour chaque nouvelle partie

    def handle_turn(self):
        """Tour du joueur"""
        #Tour du joueur 1 puis tour du joueur 2
        for i in [0,1]:
            player_list = [self.player_1_units, self.player_2_units]
            for selected_unit in player_list[i] :

                # Tant que l'unité n'a pas terminé son tour
                has_acted = False
                selected_unit.is_selected = True
                selected_unit.skill_used = False
                self.flip_display()
                
                while not has_acted:

                    # Important: cette boucle permet de gérer les événements Pygame
                    for event in pygame.event.get():

                        # Gestion de la fermeture de la fenêtre
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        # Gestion des touches du clavier
                        if event.type == pygame.KEYDOWN:

                            # Déplacement (touches fléchées)
                            dx, dy = 0, 0
                            if event.key == pygame.K_LEFT :
                                dx = -1
                            elif event.key == pygame.K_RIGHT :
                                dx = 1
                            elif event.key == pygame.K_UP :
                                dy = -1
                            elif event.key == pygame.K_DOWN :
                                dy = 1

                            selected_unit.move_PM(dx, dy, Game.ENTREE)  #change la valeur de xpm et ypm cad les coord du rect jaune
                            
                             
                            if event.key == pygame.K_RETURN:  #on a choisie une position
                                selected_unit.move() #change la valeur des coord de x et y cad l image 
                                Game.ENTREE += 1 #on a appuye sur entree
                            
                            self.flip_display()

                            # Attaque (touche espace) met fin au tour
                            if event.key == pygame.K_SPACE:

                                has_acted = True
                                selected_unit.is_selected = False
                                Game.ENTREE=0 #reenit ENTREE
                            
                            if event.key == pygame.K_a and not selected_unit.skill_used:
                                
                                selected_unit.skill_1(self)
                                
                                for unit in self.player_1_units + self.player_2_units :
                                    if unit.health <= 0 :
                                        if unit.team == 'player_1' :
                                            self.player_1_units.remove(unit)
                                        else :
                                            self.player_2_units.remove(unit)
                                            
                                self.flip_display()
                                selected_unit.skill_used = True
                                
    def flip_display(self):
        """Affiche le jeu."""

        # Affiche la grille

        self.grid_flip_display()
             
        #on l'appelle ici pour que les pieges soient au dessus des cases noires
        self.trap.draw_trap(self.screen)                

        # Affiche les unités
        self.unit_flip_display()
            

        # Rafraîchit l'écran
        pygame.display.flip()


    def grid_flip_display(self):
        
        self.screen.fill(BLACK)
        for x in range(0, WIDTH-500, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
                    
    def unit_flip_display(self):
        
        for unit in self.player_1_units + self.player_2_units:
            if unit.team == 'player_1':
                pygame.draw.rect(self.screen, GREEN, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else :
                pygame.draw.rect(self.screen, RED, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            if unit.is_selected :
                pygame.draw.rect(self.screen, YELLOW, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
            unit.draw(self.screen,Game.ENTREE)
            
            
def main():

    # Initialisation de Pygame
    pygame.init()

    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("League Of Legends")

    # Instanciation du jeu
    game = Game(screen)

    # Boucle principale du jeu, un tour comprend les 2 joueurs
    while True:
        game.handle_turn()


if __name__ == "__main__":
    main()
