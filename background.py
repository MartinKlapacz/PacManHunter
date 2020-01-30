import pygame
import random
import window_var as var
import player_module
import level_module

#Klassen für die Hintergrundgrafiken:

class Ground:

    def update(self):
        pygame.draw.rect(var.game_window,var.green,((0,var.y_position_bottom),(var.game_size[0],var.game_size[1] - var.y_position_bottom)))


class Cloud:
    
    def __init__(self, speed):
        self.y_position = random.randint(10,var.y_position_bottom - 200)
        self.cloud_pic = pygame.image.load("graphics/cloud.png")
        self.x_position = random.randint(10,var.game_size[0])
        self.speed = speed
        
    def move(self):
        self.x_position -= self.speed
        if self.x_position < -100:
            self.x_position = var.game_size[0]
            self.y_position = random.randint(10,200)

    def update(self):
        self.move()
        var.game_window.blit(self.cloud_pic,(self.x_position,self.y_position))


class House:

    def __init__(self, speed):
        self.speed = speed
        self.x_position = random.randint(0,var.game_size[0])
        self.y_position = random.randint(var.y_position_bottom,var.game_size[1])
        self.house_pic = pygame.image.load("graphics/house1.png")

    def move(self):
        self.x_position -= self.speed
        if self.x_position < -100:
            self.x_position = var.game_size[0] + random.randint(0, var.game_size[0]*0.3)
            self.y_position = random.randint(var.y_position_bottom,var.game_size[1])

    def update(self):
        self.move()
        var.game_window.blit(self.house_pic,(self.x_position,self.y_position - 50))


class Sun:
    
    def __init__(self):
        self.x_position = var.game_size[0]*0.8
        self.y_position = var.game_size[1]*0.05
        self.sun_pic = pygame.image.load("graphics/sun.png")
        
    def update(self):
        var.game_window.blit(self.sun_pic,(self.x_position,self.y_position))




#Beschriftung oben links auf dem Bildschrim:
class ScoreBoard:

    def display_scoreboard(self):
        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render("Score:  " + str(player_module.player.score)  +   "       Health: " + str(player_module.player.health) + "       Level:  " + str(level_module.levels(player_module.player.score)) , True, (0, 255, 0))
        var.game_window.blit(text, (var.game_size[0]*0.02,var.game_size[1]*0.02))


#Bild, das beim GameOver auftaucht:
def  game_over_window():
    if player_module.player.score != 300:
        var.game_window.fill((0,0,0))
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render("Game Over!", True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        var.game_window.blit(text, textrect)
        
        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render("Your score:  {} points".format(player_module.player.score), True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        textrect[1] += 30
        var.game_window.blit(text, textrect)



#Bild, das bei einer verlorenen Runde auftaucht:
def win():
    if player_module.player.score == 300:
        var.game_window.fill((255,255,255))
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render("You won!", True, (255, 250, 0))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        var.game_window.blit(text, textrect)
        
        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render("Your score:  {} points".format(player_module.player.score), True, (255, 255,0))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        textrect[1] += 30
        var.game_window.blit(text, textrect)
        
        


        
