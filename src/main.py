import pygame
from src.game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game("test du jeu", 1360, 1080)
    game.run()
