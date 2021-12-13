import sys

import pygame

def chek_event():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    """update images on the screen and flip to the new screen"""
    #redraw the screen during each through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #make the most recently drawn screen visible.
    pygame.display.flip()