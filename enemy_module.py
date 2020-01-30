import pygame
import sys
import random
import window_var as var
import player_module
import collision_detection as col
import shot_module
import time_module

class Enemy_model1:
    
    def __init__(self, number):
        self.game_window = var.game_window
        self.hitbox = [30,30]
        self.position = [var.game_size[0] + var.game_size[0]* 0.3 * number ,random.randint(0, var.flight_level)]
        self.speed = 2
        self.enemy1_image = pygame.image.load("graphics/enemy1.png")
        self.enemy1_explode = pygame.image.load("graphics/enemy1.png")
     

    def update(self):   #BewegungsKI der Gegner
        if self.position[0] > player_module.player.position[0]: #Falls der Gegner rechts vom Spieler ist, versucht er ihn zu erwischen
            if self.position[1] + self.hitbox[1]/2 == player_module.player.position[1]  + player_module.player.hitbox[1]/2: # Falls der Gegner auf der selben Höhe ist wie der Spieler,...
                #soll er sich direkt auf ihn zu bewegen
                self.position[0] -= self.speed 
            elif self.position[1] + self.hitbox[1]/2 < player_module.player.position[1]  + player_module.player.hitbox[1]/2: #Falls der Gegner über dem Spieler ist,...
                #soll er nach unten ausscheren
                if  self.position[0] < var.game_size[0]:
                    self.position[1] +=int(self.speed/2)
                self.position[0] -= self.speed
            elif self.position[1] + self.hitbox[1]/2 > player_module.player.position[1]  + player_module.player.hitbox[1]/2:#Falls der Gegner unter dem Spieler ist,...
                #soll er nach oben ausscheren
                if  self.position[0] < var.game_size[0]:
                    self.position[1] -=int(self.speed/2)
                self.position[0] -= self.speed
        else: #Falls der Gegner am Spieler vorbei ist,...
            #soll er sich einfach nach links bewegen
            self.position[0] -= self.speed
            
        if self.position[0] < 0: #bis er das Spielfeld verlässt....
            #und rechts neu gespawnt wird.
            self.position[0] = var.game_size[0] + 10
            self.position[1] = random.randint(0, var.flight_level)
            
        #pygame.draw.rect(self.game_window,var.enemy_color,(self.position,self.hitbox)) #HitBox
        var.game_window.blit(self.enemy1_image,(self.position[0],self.position[1])) #Grafik

    def die(self):
        self.position[0] = var.game_size[0] * 2 #Der Gegner verschwindet eigentlich nicht , er wird nur aus dem Fenster gespawnt
        var.game_window.blit(self.enemy1_explode,(self.position[0],self.position[1]))

    def check_enemy_hit(self, shot_position, own_position):
        if shot_module.attack.agressive == True:
            if col.collision_objects(shot_position, own_position) != "None": #falls es eine Kollision zwischen Schuss des Spielers und einem Gegner gibt ...
                self.die() #soll dieser verschwinden...
                player_module.player.score += 10 #, der Spieler bekommt 10 Punkte ... 
                shot_module.attack.agressive = False # und der Schuss soll auch verschwinden.

    def check_player_enemy_collision(self,enemy):
        if col.collision_objects(player_module.player, enemy) != "None":#falls es eine Kollision zwischen Spieler und  Gegner gibt ...
            player_module.player.health -=1 #verliehrt der Spieler einen Lebenspunkt ...
            var.last_collision_player_enemy = time_module.run()
            self.die() # und der Gegner stirbt.

        
            
    
enemy1 = Enemy_model1(1)
enemy2 = Enemy_model1(2)
enemy3 = Enemy_model1(3)
enemy4 = Enemy_model1(4)
enemy5 = Enemy_model1(5)

enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]



