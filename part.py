from constants import MOVE_PIXELS, SCREEN_SIZE, \
SIZE_X, SIZE_Y, walls
import pygame

from pygame import rect
from constants import PART_SIZE

class Wall:
    passable = False
    existing = True

    def __init__(self, coords):
        walls.append(self)
        self.brick = pygame.image.load("pictures/brick.jpeg")
        self.rect = pygame.Rect((coords[0], coords[1]), self.brick.get_size())

class Bullet:
    active = True

    def __init__(self, coords, direction):
        self.image = pygame.image.load("pictures/bullet.png")
        self.rect = pygame.Rect((coords[0], coords[1]), self.image.get_size())
        self.direction = direction
        
    def still_active(self, dx, dy):
        self.rect.left += dx
        self.rect.top += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.active = False

    def move(self):
        if self.active:
            if self.direction == 'u':
                self.still_active(0, - MOVE_PIXELS)
            if self.direction == 'd':
                self.still_active(0, MOVE_PIXELS)
            if self.direction == 'r':
                self.still_active(MOVE_PIXELS,0)
            if self.direction == 'l':
               self.still_active(- MOVE_PIXELS,0)
