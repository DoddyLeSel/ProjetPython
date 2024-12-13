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

    def grille_init(self):
        
        tableau = [[2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3],      # 1 pour Terrain
                   [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3],      # 2 pour Mur
                   [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3],      # 3 pour Rivière
                   [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 3, 3, 3, 3, 3],
                   [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3],
                   [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3],
                   [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
                   [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                   [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
                   [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        grille = []
        
        for i in range(len(tableau)) :
            for j in range(len(tableau[i])) :
                
                if tableau[i][j] == 1:
                    grille.append(Terrain(j,i))
                    
                elif tableau[i][j] == 2:
                    grille.append(Mur(j,i))
                    
                elif tableau[i][j] == 3:
                    grille.append(Riviere(j,i))

        return grille
    
    def activer_fumee(self, x, y, duree):
        for fumee in self.fumees:
            fumee.temps_restant()  #appel  de fumée
            
        # Filtrer les fumées pour ne garder que celles qui sont actives
            """Ajoute une zone de fumée à la grille."""
            print(f"Ajout de la fumée aux coordonnées : ({x}, {y})")
            nouvelle_fumee = fumee(x, y, duree)
            self.fumees.append(nouvelle_fumee)
        self.fumees = [fumee for fumee in self.fumees if fumee.is_active()]
        
    
    def mettre_a_jour_fumees(self):
    # Décrémente la durée de chaque fumée et supprime celles qui sont expirées.
        for fumee in self.fumees:
            fumee.temps_restant()  # Met à jour la durée de chaque fumée
        
    # Supprimer les fumées expirées
        self.fumees = [fumee for fumee in self.fumees if fumee.est_active]

        
    def draw_fumees(self, screen):
       # Dessine toutes les fumées actives sur la grille.
        for fumee in self.fumees:
            fumee.draw_case(screen)
        
        
    def draw_grille(self, screen):
        
        for selected_case in self.grille :
            selected_case.draw_case(screen)
            
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
            
        pygame.display.flip()





