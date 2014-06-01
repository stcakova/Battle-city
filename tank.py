from pygame.locals import *
import sys
import pygame
import math

from constants import SCREEN_SIZE, DIRECTIONS, MOVE_PIXELS, \
    PART_SIZE, walls
from part import Bullet


class Tank:
    alive = True
    shot_bullet = False

    def __init__(self, player, obj, direction):
        self.player = player
        self.rect = obj
        self.direction = direction
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.bullet = None

    def move(self):
        if self.alive:
            pressed = pygame.key.get_pressed()
            if pressed[K_LEFT]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'l'])
                self.direction = 'l'
                self.valid_move(-MOVE_PIXELS, 0)
            elif pressed[K_RIGHT]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'r'])
                self.direction = 'r'
                self.valid_move(MOVE_PIXELS, 0)
            elif pressed[K_UP]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'u'])
                self.direction = 'u'
                self.valid_move(0, -MOVE_PIXELS)
            elif pressed[K_DOWN]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'd'])
                self.direction = 'd'
                self.valid_move(0, MOVE_PIXELS)
            self.shoot_bullet()
            self.screen.blit(self.player, (self.rect.left, self.rect.top))

    def valid_move(self, dx, dy):
        self.rect.left += dx
        self.rect.top += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

    def shoot_bullet(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_SPACE]:
            if not self.shot_bullet:
                self.shot_bullet = True
                x = self.rect.left + PART_SIZE / 2
                y = self.rect.top + PART_SIZE / 2
                dir = self.direction
                self.bullet = Bullet([x, y], dir)
        if self.bullet:
            if self.bullet.active:
                self.bullet.move()
                self.screen.blit(self.bullet.image, (
                    self.bullet.rect.left, self.bullet.rect.top))
            else:
                self.shot_bullet = False
