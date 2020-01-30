import pygame

#alle möglichen Variablen sind in diesem Modul

game_size = (750,500)
game_running = True
time = 0
game_window = pygame.display.set_mode(game_size)
y_position_bottom = int(0.8 * game_size[1])
flight_level = int(0.75 * game_size[1])

FPS = 60

#Farben
red = (255,0,0)
green = (0,255,0)
blue = (100,0,255)
black = (0,0,0)
white = (255,255,255)
player_color = red
enemy_color = black
ground_color = green

x_change_player = 0
y_change_player = 0


last_collision_player_enemy = 0
