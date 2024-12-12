import pygame
import random

from unit import *
from warwick import *
from xerath import *
from missfortune import *
from cursor import *
from constante import *
from trap import *
from grille import *
from item import*

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

        self.player_2_units = [Warwick(6, 14, 'player_2'), Xerath(7,14, 'player_2'), MissFortune(8,14, 'player_2')]

        self.grille = Grille()
        
        self.item= Item(5) #creer les objets magique (Rod of ages)
        self.item.generer()
        
        
    def handle_turn(self):
        
        #Tour du joueur 1 puis tour du joueur 2
        all_units = list(zip(self.player_1_units, self.player_2_units))  # Paire des unités
        for perso  in all_units :
            for selected_unit in perso :

                # Tant que l'unité n'a pas terminé son tour
                has_acted = False
                selected_unit.is_selected = True
                selected_unit.skill_used = False
                selected_unit.mouvement = False     #pour controller l'affichage des cases se mouvements possibles
                
                if selected_unit.stunt :            #Passe le tour si l'unité est étourdie
                    has_acted = True
                    selected_unit.is_selected = False
                    selected_unit.stunt = False
                
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
                            
                            if event.key == pygame.K_p:
                                selected_unit.mouvement = True #on veut afficher les mouvement possibles
                            
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

                            selected_unit.move_PM(dx, dy)  #change la valeur de xpm et ypm cad les coord du rect jaune
                            
                            
                            if event.key == pygame.K_RETURN:   #on a choisie une position
                                selected_unit.move()           #change la valeur des coord de x et y cad l image 
                                selected_unit.returnn = True   #on a appuye sur entree
                                
                                self.item.is_collected(selected_unit.x, selected_unit.y)
                                
                            self.flip_display()

                            
                            if event.key == pygame.K_a and not selected_unit.skill_used:
                                
                                selected_unit.skill_1(self)
                                self.unit_remove()             
                                self.flip_display()
                                selected_unit.skill_used = True
                            
                            if event.key == pygame.K_z and not selected_unit.skill_used:
                                
                                selected_unit.skill_2(self)
                                self.unit_remove()             
                                self.flip_display()
                                selected_unit.skill_used = True
                                
                            if event.key == pygame.K_e and not selected_unit.skill_used:
                                
                                selected_unit.skill_3(self)
                                self.unit_remove()             
                                self.flip_display()
                                selected_unit.skill_used = True                                
                                
                            # Fin de tour
                            if event.key == pygame.K_SPACE:

                                has_acted = True
                                selected_unit.is_selected = False
                                selected_unit.returnn = False #reenit ENTREE
                                selected_unit.mouvement = False #reenit la touche P
                                selected_unit.fin_boost()
                                
                                
    def flip_display(self):
        """Affiche le jeu."""

        # Affiche la grille
        self.grille.draw_grille(self.screen)
        
        #affiche les objets magiques dans la grille
        self.item.draw_item(self.screen)
 
        # Affiche les unités
        self.unit_flip_display()

        # Rafraîchit l'écran
        pygame.display.flip()

      

    def unit_flip_display(self):
        
        for unit in self.player_1_units + self.player_2_units:
            if unit.team == 'player_1':
                pygame.draw.rect(self.screen, GREEN, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else :
                pygame.draw.rect(self.screen, RED, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            if unit.is_selected :
                pygame.draw.rect(self.screen, YELLOW, (unit.x * CELL_SIZE,unit.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
            unit.draw(self.screen)
            
    def unit_remove(self):
        for unit in self.player_1_units + self.player_2_units :
            if unit.health <= 0 :
                if unit.team == 'player_1' :
                    self.player_1_units.remove(unit)
                else :
                    self.player_2_units.remove(unit) 

    
        
        
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