import pygame
from pygame import rect

from constants import *
from part import Wall, Brick


class World:
    world = [[None for x in range(26)] for y in range(19)]

    def __init__(self):
        self.brick = pygame.image.load("pictures/brick.jpeg")
        self.wall = pygame.image.load("pictures/wall.png")
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.phoenix = pygame.image.load("pictures/phoenix.jpg")
        self.phoenix = pygame.transform.scale(
            self.phoenix, (PART_SIZE * 2, PART_SIZE * 2))

    def extract_world(self, multiplayer):
        if not multiplayer:
            maps = open(MAP)
        else:
            maps = open(MULTIPLAYER_MAP)
        for height, line in enumerate(maps):
            for width, element in enumerate(line):
                if element == 'B' or element == 'F':
                    self.world[height][width] = Wall(
                        (width * PART_SIZE, height * PART_SIZE))
                elif element == '#':
                    self.world[height][width] = Brick(
                        (width * PART_SIZE, height * PART_SIZE))

    def draw_world(self, multiplayer):
        for wall in walls:
            if wall.existing:
                wall.draw()

        self.screen.blit(self.phoenix, (440, 640))
        if multiplayer:
            self.screen.blit(self.phoenix, (440, 0))
