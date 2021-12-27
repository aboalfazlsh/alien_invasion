import pygame
class Ship():
    def __init__(self,ai_setting,screen):
        #initialize the ship and set its starting position.
        self.screen = screen
        self.ai_settings=ai_setting



        #Load the ship image and get its rect.
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # store a decimal value for the ships center.
        self.center = float(self.rect.centerx)
        self.bottm= float(self.rect.bottom)

        #Start each new ship  at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ update the ships position based on the movement flag"""
        #update the ships center value , not the rect
        if self.moving_right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_up:
            self.bottm -= self.ai_settings.ship_speed_factor
        elif self.moving_down:
            self.bottm += self.ai_settings.ship_speed_factor

        #update rect object form self.center.
        self.rect.centerx=self.center
        self.rect.bottom=self.bottm

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)