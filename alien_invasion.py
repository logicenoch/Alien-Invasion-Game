import sys
import pygame
from settings import Settings


def run_game():
    #initiate game and create the object screen.
    """
    @init() initializes background settings that pygame
    needs to work properly.
    """
    pygame.init()
    ai_settings = Settings()
    #screen is an object of the class "surface"
    #where you display a game element.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_width))

    pygame.display.set_caption("Alien Invasion By Logic")

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse event
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
        #Make the most recently drawn screen visible
        pygame.display.flip()


run_game()