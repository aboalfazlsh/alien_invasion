import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
def run_game():
    #initilize pygame, setting and screen object.
    pygame.init()
    ai_setting=Settings()
    screen=pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship = Ship(screen)

    #set the background color
    #bg_color=(50,230,185)
    #start the main loop for game .
    while True:

        #function for Watch for keyboard and mouse evevnts.
        gf.chek_event(ship)
        ship.update()
        gf.update_screen(ai_setting,screen,ship)



run_game()