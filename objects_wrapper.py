from pygame.locals import *
import pygame

from tank import Tank
from part import Bullet
from constants import *


class TankWrapper(Tank):

    def __init__(self,  coords, direction, phoenix, image=None, enemy=None):
        self.player = pygame.image.load(image).convert_alpha()
        self.player = pygame.transform.scale(
            self.player, (PART_SIZE, PART_SIZE))
        self.direction = direction
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.phoenix = phoenix
        self.enemy = enemy
        Tank.__init__(self, coords, self.direction, self.phoenix, self.enemy)

    def update_tank1(self):
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

    def update_tank2(self):
        if self.alive:
            pressed = pygame.key.get_pressed()
            if pressed[K_a]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'l'])
                self.direction = 'l'
                self.valid_move(-MOVE_PIXELS, 0)

            elif pressed[K_d]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'r'])
                self.direction = 'r'
                self.valid_move(MOVE_PIXELS, 0)

            elif pressed[K_w]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'u'])
                self.direction = 'u'
                self.valid_move(0, -MOVE_PIXELS)

            elif pressed[K_s]:
                self.player = pygame.transform.rotate(
                    self.player, DIRECTIONS[self.direction + 'd'])
                self.direction = 'd'
                self.valid_move(0, MOVE_PIXELS)

            self.shoot_bullet_player2()
        self.screen.blit(self.player, (self.rect.left, self.rect.top))

    def update_enemy(self):
        self.move_enemy()
        self.screen.blit(self.player, (self.rect.left, self.rect.top))

    def shoot_bullet(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RCTRL]:
            if not self.shot_bullet:
                self.update_bullet()
        if self.bullet:
            if self.bullet.active:
                self.bullet.move(self.enemy)
                self.screen.blit(self.bullet.image, (
                    self.bullet.rect.left, self.bullet.rect.top))
            else:
                self.shot_bullet = False

    def rotate_player(self, direction):
        self.player = pygame.transform.rotate(
            self.player, DIRECTIONS[self.direction + direction])
        self.direction = direction

    def shoot_bullet_player2(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LCTRL]:
            if not self.shot_bullet:
                self.update_bullet()
        if self.bullet:
            if self.bullet.active:
                self.bullet.move(self.enemy)
                self.screen.blit(self.bullet.image, (
                    self.bullet.rect.left, self.bullet.rect.top))
            else:
                self.shot_bullet = False


class BulletWrapper(Bullet):

    def __init__(self):
        self.image = pygame.image.load("pictures/bullet.png")
        self.rect = pygame.Rect((coords[0], coords[1]), self.image.get_size())
        self.direction = direction
        Bullet.__init__(self, (coords[0], coords[1]), self.direction)

    def create_bullet(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RCTRL]:
            self.shoot_bullet()
