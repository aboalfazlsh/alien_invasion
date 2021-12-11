import sys
import pygame
from settings import Settings
def run_game():
    #initilize pygame, setting and screen object.
    pygame.init()
    ai_setting=Settings()
    screen=pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    #set the background color
    #bg_color=(50,230,185)
    #start the main loop for game .
    while True:

        #Watch for keyboard and mouse evevnts.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass through the loop
        screen.fill(ai_setting.bg_color)
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()