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
        gf.chek_event()

        #redraw the screen during each pass through the loop
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()