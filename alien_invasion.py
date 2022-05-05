import sys
import pygame

def run_game():
    #initiate game and create the object screen
    """
    @init() initializes background settings that pygame
    needs to work properly.
    """
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion By Logic")

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()