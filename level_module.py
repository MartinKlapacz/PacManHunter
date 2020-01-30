import pygame
import player_module
import time
import window_var as var
import time_module

#Hilfsvariablen die dafür da sind, damit die levelscreens nur einmal auftauchen
l100 = True
l200 = True
l300 = True

def levels(score):  #Ermittlung des momentanen Levels
    global level
    if score >= 0:
        level = 1
        if score >= 100:
            level = 2  
            if score >= 200:
                level = 3
        return level


def level_screen(score):
    global level
    global l100
    global l200
    global l300
    if score == 100 and l100 == True:
        basicfont = pygame.font.SysFont(None, 50)
        text = basicfont.render("Level: {}".format(score), True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        var.game_window.blit(text, textrect)
        time.sleep(1)
        l100 = False #Pause soll nur einmal stattfinden
        player_module.player.health += 2 #Lebenspunkte werden um 2 erhöht
    if score == 200 and l200 == True:
        basicfont = pygame.font.SysFont(None, 50)
        text = basicfont.render("Level: {}".format(score), True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = var.game_window.get_rect().centerx
        textrect.centery = var.game_window.get_rect().centery
        var.game_window.blit(text, textrect)
        time.sleep(1)
        l200 = False #Pause soll nur einmal stattfinden
        player_module.player.health += 2 #Lebenspunkte werden um 2 erhöht

