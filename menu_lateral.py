import pygame

from constante import *

class Menu_Lateral():
    
    def __init__(self, unit):
        
        self.x = GRID_SIZE * CELL_SIZE
        self.y = 0
        self.unit = unit
        
    def draw_menu(self):
        
        pygame.draw.rect(Game.instance.screen, MENU_BLEU, (self.x, self.y, MENU_WIDTH, GRID_SIZE * CELL_SIZE))
        
        pygame.draw.rect(Game.instance.screen, WHITE, (self.x + 20, self.y + 20, 220, 110), 2) #Haut gauche
        pygame.draw.rect(Game.instance.screen, WHITE, (self.x + 260, self.y + 20, 220, 110), 2) #Haut droit
        pygame.draw.rect(Game.instance.screen, WHITE, (self.x + 20, self.y + 150, 220, 110), 2) #Bas gauche
        pygame.draw.rect(Game.instance.screen, WHITE, (self.x + 260, self.y + 150, 220, 110), 2) #Bas droit
        
        image1 = pygame.image.load(self.unit.skill_1_img).convert_alpha()    #Skill 1
        image1 = pygame.transform.scale(image1, (106, 106))
        screen.blit(image1, (self.x + 262, self.y + 22))
        
        image2 = pygame.image.load(self.unit.skill_2_img).convert_alpha()    #Skill 2
        image2 = pygame.transform.scale(image2, (106, 106))
        screen.blit(image2, (self.x + 22 , self.y + 262))
        
        image3 = pygame.image.load(self.unit.skill_3_img).convert_alpha()    #Skill 3
        image3 = pygame.transform.scale(image3, (106, 106))
        screen.blit(image3, (self.x + 262, self.y + 262))
        
        pygame.flip.display()
        
    