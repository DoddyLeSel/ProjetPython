from .mur import *
from .riviere import *
from .terrain import *
from .fumee import *

from constante import *

class Grille:
    
    def __init__(self):
        
        self.width = CELL_SIZE * GRID_SIZE 
        self.height = CELL_SIZE * GRID_SIZE 
        self.grille = self.grille_init()
        self.fumees=[]
        self.tableau=[]

    def grille_init(self):
        
        self.tableau = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # 1 pour Terrain
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # 2 pour Mur
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # 3 pour Rivière
                        [1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        grille = []
        
        for i in range(len(self.tableau)) :
            for j in range(len(self.tableau[i])) :
                
                if self.tableau[i][j] == 1:
                    grille.append(Terrain(j,i))
                    
                elif self.tableau[i][j] == 2:
                    grille.append(Mur(j,i))
                    
                elif self.tableau[i][j] == 3:
                    grille.append(Riviere(j,i))

        
        return grille
    
    def activer_fumee(self, x, y, duree):
        """
        Ajoute une fumée temporaire à la grille.
        """
        nouvelle_fumee = Fumee(x, y,duree)
        nouvelle_fumee.duree = duree  # Définit la durée de la fumée
        self.grille.append(nouvelle_fumee)
      
    def mettre_a_jour_fumees(self):
        """
        Met à jour les fumées en réduisant leur durée et en les supprimant si elles disparaissent.
        """
        fumee_a_supprimer = []
        for case in self.grille:
            if isinstance(case, Fumee):
                case.duree -= 1
                if case.duree <= 0:
                    fumee_a_supprimer.append(case)
        for fumee in fumee_a_supprimer:
            self.grille.remove(fumee)
    
        
        
    def draw_grille(self, game):
        
        for selected_case in self.grille :
            selected_case.draw_case(game)
            
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(game.screen, WHITE, rect, 1)
            
        pygame.display.flip()





