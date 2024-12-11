from case import *
from constante import *

class riviere(case):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.couleur=WHITE
        self.accessible=True
        
    def dessiner(self, screen):
        # Charge une image pour représenter la rivière
        image = pygame.image.load("img/riviere.png").convert_alpha()
        image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))