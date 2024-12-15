import pygame
import random

from units import *
from board import *

from constante import *
from menu_lateral import *

from trap import *
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
        La liste des unités du joueur 1
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

        self.player_1_units = [Warwick(6, 13, 'player_1'), Xerath(7,13, 'player_1'), MissFortune(8,13, 'player_1')]


        self.player_2_units = [Warwick(6, 14, 'player_2'), Xerath(7,14, 'player_2'), MissFortune(8,14, 'player_2')]

        self.grille = Grille()
        self.grille.activer_fumee(10, 10, 3)  # Active une fumée sur la case (10, 10) pendant 3 tours
        self.grille.activer_fumee(11, 10, 3)   # Active une fumée sur la case (11, 10) pendant 3 tours


        self.menu = Menu_Lateral()
        self.messages = []
        
        self.grille.activer_fumee(3, 10, 10)     
        self.grille.activer_fumee(3, 4, 10)                      
        self.grille.mettre_a_jour_fumees()
        
        self.item= Item() #creer les objets magique (Rod of ages)
        
        self.pos_unit = {(6,1),(7,1),(8,1),(6,14),(7,14),(8,14)} #set des positions initiales de toutes les unités
        
    def handle_turn(self):
        
        #Tour du joueur 1 puis tour du joueur 2
        for i in [0,1]:
            player_list = [self.player_1_units, self.player_2_units]
            
            self.messages.append("------ Nouveau Tour ------")
            
            for selected_unit in player_list[i] :
                
                self.messages.append("------ Nouvelle unité ------")
                
                self.selected_unit = selected_unit
                
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

                        self.unit_remove()
                        
                        # Gestion de la fermeture de la fenêtre
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        # Gestion des touches du clavier
                        
                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_o and selected_unit.has_item == True: # utiliser l'objet magique en appuyant sur "o"
                                self.item.recover(selected_unit) 
                            
                            if event.key == pygame.K_p:
                                selected_unit.mouvement = True # appuyer sur p pour afficher les mouvements possibles
                            
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
                                
                                self.pos_unit.discard((selected_unit.x,selected_unit.y)) #supprimer l'ancienne coord de l'unité
                                selected_unit.move()           #change la valeur des coord de x et y cad l image 
                                self.pos_unit.add((selected_unit.x,selected_unit.y)) #ajouter la nouvelle coord de l'unité
                                selected_unit.returnn = True   #on a appuye sur entree
                                    
                                self.item.is_collected(selected_unit,selected_unit.x, selected_unit.y)
                                
                            self.flip_display()

                            
                            if event.key == pygame.K_a and not selected_unit.skill_used:
                                
                                self.messages.append(selected_unit.name + " utilise son sort " + selected_unit.skill_1_nom)
                                self.flip_display()
                                
                                selected_unit.skill_1(self)
                                self.unit_remove()
                                self.flip_display()
                                
                                selected_unit.skill_used = True
                            
                            if event.key == pygame.K_z and not selected_unit.skill_used:
                                
                                self.messages.append(selected_unit.name + " utilise son sort " + selected_unit.skill_2_nom)
                                self.flip_display()
                                
                                selected_unit.skill_2(self)
                                self.unit_remove()             
                                self.flip_display()
                                
                                selected_unit.skill_used = True
                                
                            if event.key == pygame.K_e and not selected_unit.skill_used:
                                
                                self.messages.append(selected_unit.name + " utilise son sort " + selected_unit.skill_3_nom)
                                self.flip_display()
                                
                                selected_unit.skill_3(self)
                                self.unit_remove()             
                                self.flip_display()
                                
                                selected_unit.skill_used = True                                
                                
                            # Fin de tour
                            if event.key == pygame.K_SPACE:

                                has_acted = True
                                selected_unit.is_selected = False
                                selected_unit.returnn = False        #reinit la touche ENTREE
                                selected_unit.mouvement = False      #reinit la touche P
                                selected_unit.reinitialiser_PM()     #reinit les valeurs des PM et les modifier si y a eu un passage par une riviere
                                selected_unit.fin_boost()            #Met fin aux boost de PM et d'attaque à la fin du tour
                                
        # Mettre à jour les fumées après chaque tour complet
            self.grille.mettre_a_jour_fumees()
    
                                
                                  
                                
                                
    def flip_display(self):
        """Affiche le jeu."""

        # Affiche la grille
        self.grille.draw_grille(self)
              
        #affiche les objets magiques dans la grille
        self.item.draw_item(self.screen)
 
        # Affiche les unités
        self.unit_flip_display()

        self.menu.draw_menu(self)
        
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
                
            unit.draw(self.screen,self.grille.grille,self.pos_unit)
            
    def unit_remove(self):
        
        font = pygame.font.Font(None, 200)
        
        if len(self.player_1_units) == 0 :
            text0 = font.render("Défaite", True, WHITE)
            text0_rect = text0.get_rect(center= pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT)).center)
            self.screen.blit(text0, text0_rect)
            pygame.display.flip()
        
        elif len(self.player_2_units ) == 0 :
            text1 = font.render("Victoire", True, WHITE)
            text1_rect = text1.get_rect(center= pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT)).center)
            self.screen.blit(text1, text1_rect)
            pygame.display.flip()
            
        for unit in self.player_1_units + self.player_2_units :
            if unit.health <= 0 :
                if unit.team == 'player_1' :
                    self.player_1_units.remove(unit)
                else :
                    self.player_2_units.remove(unit)
                    
                self.messages.append(unit.name + " est mort")

    
        
        
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