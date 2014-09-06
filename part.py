from constants import *
import pygame

from pygame import rect
from constants import PART_SIZE


class Wall:
    passable = True
    existing = True

    def __init__(self, coords):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        walls.append(self)
        self.brick = pygame.image.load("pictures/brick.jpeg")
        self.rect = pygame.Rect((coords[0], coords[1]), self.brick.get_size())

    def draw(self):
        self.screen.blit(self.brick, (self.rect.left, self.rect.top))


class Brick:
    passable = False
    existing = True

    def __init__(self, coords):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        walls.append(self)
        self.wall = pygame.image.load("pictures/wall.png")
        self.rect = pygame.Rect((coords[0], coords[1]), self.wall.get_size())

    def draw(self):
        self.screen.blit(self.wall, (self.rect.left, self.rect.top))


class Bullet:
    active = True

    def __init__(self, coords, direction):
        self.image = pygame.image.load("pictures/bullet.png")
        self.rect = pygame.Rect((coords[0], coords[1]), self.image.get_size())
        self.direction = direction

    def still_active(self, dx, dy, enemies=None):
        self.rect.left += dx
        self.rect.top += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.active = False
                if wall.passable:
                    wall.existing = False
                    walls.remove(wall)

        for enemy in enemies:
            if self.rect.colliderect(enemy):
                self.active = False
                if enemy.phoenix[1] == 640:
                    enemy.rect.left = 300
                    enemy.rect.top = 380
                elif enemy.phoenix[1] == 0:
                    enemy.rect.left = 580
                    enemy.rect.top = 380
            if (self.rect.top >= enemy.phoenix[1] and
               self.rect.top <= enemy.phoenix[1] + 2 * PART_SIZE and
               self.rect.left >= enemy.phoenix[0] and
               self.rect.left <= enemy.phoenix[0] + 2 * PART_SIZE):
                self.active = False
                enemy.alive = False

    def move(self, enemy):
        if self.active:
            if self.direction == 'u':
                self.still_active(0, - MOVE_PIXELS - 5, enemy)
            if self.direction == 'd':
                self.still_active(0, MOVE_PIXELS + 5, enemy)
            if self.direction == 'r':
                self.still_active(MOVE_PIXELS + 5, 0, enemy)
            if self.direction == 'l':
                self.still_active(- MOVE_PIXELS - 5, 0, enemy)
