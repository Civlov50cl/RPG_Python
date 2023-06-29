import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game("Nom du jeu", 136, 157)
    game.run()
