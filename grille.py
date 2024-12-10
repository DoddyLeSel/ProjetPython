from case import *
class Grille:
    def __init__(self, taille):
        self.taille = taille 
        self.cases = self.creer_grilles() 

    def creer_grilles(self):
        
        grille = [[case(x, y) for x in range(self.taille)] for y in range(self.taille)]
        return grille

    def dessiner(self, surface):
        # Dessine la grille et les cases sur la fenêtre Pygame
        TAILLE_CASE = 50  
        for ligne in self.cases:
            for case in ligne:
                pygame.draw.rect(
                    surface,
                    case.couleur,
                    (case.x * TAILLE_CASE, case.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE),
                )
        # Ajout des lignes de la grille
        COULEUR_LIGNE = (255, 255, 255)  # Noir pour les lignes
        for i in range(self.taille + 1):
            pygame.draw.line(surface, COULEUR_LIGNE, (0, i * TAILLE_CASE), (self.taille * TAILLE_CASE, i * TAILLE_CASE))
            pygame.draw.line(surface, COULEUR_LIGNE, (i * TAILLE_CASE, 0), (i * TAILLE_CASE, self.taille * TAILLE_CASE))




