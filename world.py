import pygame
from pygame import rect
from constants import *
from part import  Wall


class World:
    world = [[None for x in range(50)] for y in range(50)]

    def __init__(self):
        self.brick = pygame.image.load("pictures/brick.jpeg")
        self.wall = pygame.image.load("pictures/wall.png")
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.phoenix = pygame.image.load("pictures/phoenix.jpg")
        self.phoenix = pygame.transform.scale(
            self.phoenix, (PART_SIZE*2, PART_SIZE*2))

    def draw_world(self):
        maps = open(MAP)
        for height, line in enumerate(maps):
            for width, element in enumerate(line):
                if element != '\n' and element != '_':
                    self._draw_element(element, (width* PART_SIZE, height*PART_SIZE))

    def _draw_element(self, letter, coords):
        self.screen.blit(self.phoenix, (440, 640))
        if letter == 'B':
            self.screen.blit(self.brick, (coords[0], coords[1]))
            Wall(coords)
        elif letter == '#':
            self.screen.blit(self.wall, (coords[0], coords[1]))
            Wall(coords)
