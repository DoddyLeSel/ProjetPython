import pygame

from constante import *

class Menu_Lateral():
    
    def __init__(self):
        
        self.x = GRID_SIZE * CELL_SIZE
        self.y = 0


    def draw_menu(self, game):
        
        pygame.draw.rect(game.screen, MENU_BLEU, (self.x, self.y, MENU_WIDTH, GRID_SIZE * CELL_SIZE))
        
        pygame.draw.rect(game.screen, WHITE, (self.x + 20, self.y + 20, 220, 70), 2)     #Haut gauche
        pygame.draw.rect(game.screen, WHITE, (self.x + 260, self.y + 20, 220, 70), 2)    #Haut droit
        pygame.draw.rect(game.screen, WHITE, (self.x + 20, self.y + 110, 220, 70), 2)    #Bas gauche
        pygame.draw.rect(game.screen, WHITE, (self.x + 260, self.y + 110, 220, 70), 2)   #Bas droit
        
        font = pygame.font.Font(None, 18)
        
        image0 = pygame.image.load("img/Deplacement.png").convert_alpha()    #Déplacement
        image0 = pygame.transform.scale(image0, (66, 66))
        game.screen.blit(image0, (self.x + 22, self.y + 22))
        text0 = font.render("P : Déplacement", True, WHITE)
        text0_rect = text0.get_rect(center= pygame.draw.rect(game.screen, WHITE, (self.x + 88, self.y + 20, 152, 70), 2).center)
        game.screen.blit(text0, text0_rect)


        image1 = pygame.image.load(game.selected_unit.skill_1_img).convert_alpha()    #Skill 1
        image1 = pygame.transform.scale(image1, (66, 66))
        game.screen.blit(image1, (self.x + 262, self.y + 22))
        text1 = font.render("A : " + game.selected_unit.skill_1_nom, True, WHITE)
        text1_rect = text1.get_rect(center= pygame.draw.rect(game.screen, WHITE, (self.x + 328, self.y + 20, 152, 70), 2).center)
        game.screen.blit(text1, text1_rect)
        
        
        image2 = pygame.image.load(game.selected_unit.skill_2_img).convert_alpha()    #Skill 2
        image2 = pygame.transform.scale(image2, (66, 66))
        game.screen.blit(image2, (self.x + 22 , self.y + 112))
        text2 = font.render("Z : " + game.selected_unit.skill_2_nom, True, WHITE)
        text2_rect = text2.get_rect(center= pygame.draw.rect(game.screen, WHITE, (self.x + 88, self.y + 110, 152, 70), 2).center)
        game.screen.blit(text2, text2_rect)
        
        
        image3 = pygame.image.load(game.selected_unit.skill_3_img).convert_alpha()    #Skill 3
        image3 = pygame.transform.scale(image3, (66, 66))
        game.screen.blit(image3, (self.x + 262, self.y + 112))
        text3 = font.render("E : " + game.selected_unit.skill_3_nom, True, WHITE)
        text3_rect = text3.get_rect(center= pygame.draw.rect(game.screen, WHITE, (self.x + 328, self.y + 110, 152, 70), 2).center)
        game.screen.blit(text3, text3_rect)
        
        pygame.draw.line(game.screen, WHITE, (self.x, self.y + 200), (self.x + MENU_WIDTH, self.y + 200))
        
        y_offset = 210
        
        if len(game.messages) > 15 :
            game.messages.pop(0)
        
        for message in game.messages:
            text_surface = font.render(message, True, WHITE)  # Texte blanc
            game.screen.blit(text_surface, (self.x + 10, y_offset))
            y_offset += 30
        
        
        pygame.display.flip()



class Console:
    
    def init(self, screen):
        """
        Initialise la console avec une barre verticale pour les messages.
        """
        self.screen = screen  # L'écran Pygame sur lequel dessiner
        self.messages = []  # Liste pour stocker les messages récents

    def add_message(self, message):
        """
        Ajoute un message à la liste des messages récents.
        """
        self.messages.append(message)
        if len(self.messages) > 10:  # Limiter à 10 messages affichés
            self.messages.pop(0)

    def draw_message_bar(self):
        """
        Dessine la barre verticale et affiche les messages.
        """
        bar_width = 200
        bar_x = WIDTH  # Position x de la barre noire (à droite de la grille)

        pygame.draw.rect(self.screen, (0, 0, 0), (bar_x, 0, bar_width, HEIGHT))  # Barre noire

        font = pygame.font.Font(None, 24)
        y_offset = 10
        
        for message in self.messages:
            text_surface = font.render(message, True, (255, 255, 255))  # Texte blanc
            self.screen.blit(text_surface, (bar_x + 10, y_offset))
            y_offset += 30    