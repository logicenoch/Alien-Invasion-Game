import sys
from turtle import bgcolor
import pygame

def run_game():
    #initiate game and create the object screen.
    """
    @init() initializes background settings that pygame
    needs to work properly.
    """

    pygame.init()
    #screen is an object of the class "surface" 
    #where you display a game element.
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion By Logic")
    bg_color = (230,230,230)

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse event
        for event in pygame.event.get():
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
        #Make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()