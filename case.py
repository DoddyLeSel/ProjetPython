import pygame
TAILLE_CASE=50 
class case:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.couleur=(0,0,0)
        self.accessible= True
    def dessiner(self, surface):
        """Dessiner la case sur le plateau."""
        pygame.draw.rect(surface,self.couleur,(self.x * TAILLE_CASE, self.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE) )
        





