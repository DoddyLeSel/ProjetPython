import pygame
from constante import *





#Des objets magiques que les persos peuvent collecter et utiliser en appuyant sur la touche "o"
class Item:
    
    def __init__(self):
        
        
        #Hérite de la classe Case
        self.positions = {(0,7),(8,7),(15,6),(15,10)}
        
    


    def draw_item(self, screen):
        
        for  x, y in self.positions:
            # Affiche une image ou un rectangle pour représenter le piège
            image = pygame.image.load("img/RodOfAges.JPG").convert_alpha()
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            screen.blit(image, (x * CELL_SIZE,y * CELL_SIZE))
    
    def is_collected (self,unit,x,y):
        
        if (x,y) in self.positions : #verifier si le perso est sur la case de l'objet
            unit.has_item = True #le perso possède un objet 
            self.positions.discard((x,y)) #supprimer les coord de l objet du set

    def recover(self,unit)   :

        if unit.health < 100 :
            unit.health = unit.health +20
        else :
            unit.health = 100    
            


