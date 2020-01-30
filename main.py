import pygame

import background
import window_var as var
import player_module
import enemy_module
import collision_detection as col
import shot_module
import time_module
import level_module

pygame.init()
pygame.display.set_caption("PacManHunter")
var. game_window = pygame.display.set_mode(var.game_size)
clock = pygame.time.Clock()

#Instanzen der Klassen House, Cloud und Sun
ground = background.Ground()
sun = background.Sun()
cloud_1 = background.Cloud(1)
cloud_2 = background.Cloud(2)
cloud_3 = background.Cloud(1.5)
house_1 = background.House(2)
house_2 = background.House(2)
house_3 = background.House(2)
score_board = background.ScoreBoard()

shot_in_the_air = False



while var.game_running:
    time_module.run()     #Zeitmessung bei jeder Runde
    level_module.levels(player_module.player.score)
    level_module.level_screen(player_module.player.score)
      
    # Hintergrundgrafiken
    var.game_window.fill(var.blue)     
    ground.update()
    sun.update() 
    cloud_1.update()
    cloud_2.update()
    cloud_3.update()
    house_1.update()
    house_2.update()
    house_3.update()
    
    for event in pygame.event.get():    #Input zur Steuerung der Spielerbewegung
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                var.x_change_player = -4
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                var.x_change_player = 3
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                var.y_change_player = -3
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                var.y_change_player = 3
            elif event.key == pygame.K_SPACE:
                shot_module.attack.shot_in_the_air = True
        if event.type == pygame.KEYUP:
            var.x_change_player = 0
            var.y_change_player = 0

    #Test Kollisionen mit Gegner
    for i in enemy_module.enemy_list:
        i.check_player_enemy_collision(i)

    #Schuesse der Gegner
    for i in range(len(enemy_module.enemy_list)):
        shot_module.enemy_attack_list[i].update(i)

    #Test ob Spieler getroffen wird
    for i in range(len(shot_module.enemy_attack_list)):
          if col.collision_objects(player_module.player,shot_module.enemy_attack_list[i]) != "None":
               player_module.player.health -= 1
               shot_module.enemy_attack_list[i].position[0] = 0
               
    #Test ob Gegner getroffen
    for i in enemy_module.enemy_list:
        i.check_enemy_hit(shot_module.attack,i)
        
    #Darstellung der Schuesse des Spielers
    shot_module.attack.update()
    
    #Spielcharaktere   
    player_module.player.update(var.x_change_player,var.y_change_player)
    enemy_module.enemy1.update()
    enemy_module.enemy2.update()
    enemy_module.enemy3.update()
    enemy_module.enemy4.update()
    enemy_module.enemy5.update()

    score_board.display_scoreboard()#Scoreboard 
    clock.tick(var.FPS)

    level_module.levels(player_module.player.score)
    level_module.level_screen(player_module.player.score)

    background.win() #Test ob das Spiel gewonnen wurde
        
    pygame.display.update()

background.game_over_window() #Darstellung des GameOverscreens

pygame.display.update()
