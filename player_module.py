import pygame
import sys
import random
import window_var as var
import collision_detection as col
import time


class Player:
     
     def __init__(self):
          self.game_window = var.game_window
          self.hitbox = [30,15]
          self.position = [int(var.game_size[0]*0.05),int(var.game_size[1]*0.5)]
          self.player_bottom = self.position[1] + self.hitbox[1]
          self.player_top = self.position[1]
          self.player_right = self.position[0] + self.hitbox[0]
          self.player_left = self.position[0]
          self.speed = 8
          self.health = 3
          self.score = 0
          self.player_image = pygame.image.load("graphics/player.png")

     def update(self,x_change_player,y_change_player):
          self.player_bottom = self.position[1] + self.hitbox[1]
          self.player_top = self.position[1]
          self.player_right = self.position[0] + self.hitbox[0]
          self.player_left = self.position[0]

          if self.health > 0:     
               #Beweglichkeit des Spielers nur innerhalb des Flugbereiches möglich
               if not (self.player_left < 0 and x_change_player < 0):             #Höhe
                    if not (self.player_right > var.game_size[0] and x_change_player > 0):
                         self.position[0] = self.position[0] + x_change_player
               if not (self.player_top < 0 and y_change_player < 0):            #Breite
                    if not (self.player_bottom > var.flight_level and y_change_player > 0):
                         self.position[1] += y_change_player
               #pygame.draw.rect(self.game_window,var.player_color,(self.position,self.hitbox)) #HitBox
               var.game_window.blit(self.player_image,(self.position[0],self.position[1])) #Grafik
               
          else:
               time.sleep(1)
               var.game_running = False

     def check_hit(self,i):
          if col.collision_objects(player,i) != "None":
               self.health -= 1 #Wird der Spieler getroffen, so verliert er einen Lebenspunkt
               
player = Player()
             
         
          
          
