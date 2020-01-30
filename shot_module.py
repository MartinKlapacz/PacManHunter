import pygame
import sys
import random
import window_var as var
import player_module
import enemy_module
import collision_detection as col
import time_module

class Player_Shot: #Klasse für die Schüsse des Spielers
    
    def __init__(self):
        self.hitbox = [20, 5]
        self.speed = 15
        self.position = [0,10]
        self.colour = (45,233,55)
        self.shot_in_the_air = False
        self.first_frame = True
        self.agressive = True
        
    def update(self):
        if  self.shot_in_the_air == True:
            if self.first_frame == True: #Beim ersten frame wird dem Schuss die Position des Spielers übergeben, von wo er losfliegen soll
                self.shot_time = time_module.run() #Der Zeitpunkt des Schusses wird gespeichert
                self.position[0] = player_module.player.position[0] + player_module.player.hitbox[0]
                self.distance_start = player_module.player.position[0] + player_module.player.hitbox[0]
                self.position[1] = player_module.player.position[1] + player_module.player.hitbox[1]/2
                self.agressive = True 
                self.first_frame = False
            self.position[0] += self.speed
            if self.agressive == True: #Solange er agressive ist wird er dargestellt 
                pygame.draw.rect(var.game_window,self.colour,(self.position,self.hitbox))
            if self.distance_start +  self.speed * var.FPS < self.position[0]: #Regelierung der Wartezeit für die Schüsse
                self.shot_in_the_air = False
                self.first_frame = True

# ein Schussobjekt für ein Spieler
attack = Player_Shot()



class Enemy_Shot: #Klasse für die Schüsse der Gegner
    
    def __init__(self):
        self.hitbox = [20, 5]
        self.speed = 10
        self.position = [0,0]
        self.colour = (255,0,5)
        self.shot_in_the_air = True
        self.first_frame = True
        self.agressive = True

    def update(self, i):
        if  self.shot_in_the_air == True:
            if enemy_module.enemy_list[i].position[0] < var.game_size[0]:
                if self.first_frame == True: #Beim ersten frame wird dem Schuss die Position des Spielers übergeben, von wo er losfliegen soll
                    self.position[0] = enemy_module.enemy_list[i].position[0]
                    self.distance_start = enemy_module.enemy_list[i].position[0] 
                    self.position[1] = enemy_module.enemy_list[i].position[1] + enemy_module.enemy_list[i].hitbox[1]/2
                    self.agressive = True #Der Schuss ist nicht mehr aggresive, wenn der ein Ziel trifft
                    self.first_frame = False
                self.position[0] -= self.speed
                if self.agressive == True: #Solange er agressive ist wird er dargestellt 
                    pygame.draw.rect(var.game_window,self.colour,(self.position,self.hitbox))
                if self.distance_start -  self.speed * var.FPS > self.position[0] and self.position[0] < 0: #Regelierung der Wartezeit für die Schüsse
                   self.shot_in_the_air = True
                   self.first_frame = True

            

#5 einzelne Schüsse für 5 Gegnerobjekte
enemy_attack1 = Enemy_Shot()
enemy_attack2 = Enemy_Shot()
enemy_attack3 = Enemy_Shot()
enemy_attack4 = Enemy_Shot()
enemy_attack5 = Enemy_Shot()

enemy_attack_list = [enemy_attack1,enemy_attack2,enemy_attack3,enemy_attack4,enemy_attack5]

    
