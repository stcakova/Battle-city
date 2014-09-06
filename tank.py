from pygame.locals import *
import pygame


from constants import *
from part import Bullet


class Tank:

    def __init__(self, coords, direction, phoenix=None, enemy=None):
        self.coords = coords
        self.rect = pygame.Rect((coords[0], coords[1]), (40, 40))
        self.direction = direction
        self.phoenix = phoenix
        self.enemy = enemy
        self.bullet = None
        self.score = 0
        self.alive = True
        self.shot_bullet = False

    def update_bullet(self):
        self.shot_bullet = True
        x = self.rect.left + PART_SIZE / 2
        y = self.rect.top + PART_SIZE / 2
        dir = self.direction
        self.bullet = Bullet([x, y], dir)

    def set_coordinates(self, coordinates):
        self.rect.left, self.rect.top = coordinates

    def move_left(self):
        if self.valid_move(-MOVE_PIXELS, 0):
            pass
        else:

            self.player = pygame.transform.rotate(
                self.player, DIRECTIONS[self.direction + 'd'])
            self.direction = 'd'
            self.move_down()

    def move_right(self):
        if self.valid_move(MOVE_PIXELS, 0):
            pass
        else:

            self.player = pygame.transform.rotate(
                self.player, DIRECTIONS[self.direction + 'u'])
            self.direction = 'u'
            self.move_up()

    def move_up(self):
        if self.valid_move(0, -MOVE_PIXELS):
            pass
        else:

            self.player = pygame.transform.rotate(
                self.player, DIRECTIONS[self.direction + 'l'])
            self.direction = 'l'
            self.move_left()

    def move_down(self):
        if self.valid_move(0, MOVE_PIXELS):
            pass
        else:
            self.player = pygame.transform.rotate(
                self.player, DIRECTIONS[self.direction + 'r'])
            self.direction = 'r'
            self.move_right()

    def move_enemy(self):
        if self.direction == 'l':
            self.move_left()

        elif self.direction == 'd':
            self.move_down()

        elif self.direction == 'u':
            self.move_up()

        elif self.direction == 'r':
            self.move_right()

        self.shoot_bullet_enemy()

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
                return False

        if self.enemy:
            for enemy in self.enemy:
                if self.rect.colliderect(enemy):
                    if dx > 0:
                        self.rect.right = enemy.rect.left
                    if dx < 0:
                        self.rect.left = enemy.rect.right
                    if dy > 0:
                        self.rect.bottom = enemy.rect.top
                    if dy < 0:
                        self.rect.top = enemy.rect.bottom
                    return False
        return True

    def direct_hit(self):
        for enemy in self.enemy:
            if self.rect.top == enemy.rect.top:
                if self.rect.left > enemy.rect.left:
                    self.rotate_player('l')
                else:
                    self.rotate_player('r')
                return True
            elif self.rect.left == enemy.rect.left:
                if self.rect.top > enemy.rect.top:
                    self.rotate_player('u')
                else:
                    self.rotate_player('d')
                return True
        return False

    def hit_phoenix(self):
        for enemy in self.enemy:
            if self.rect.top >= enemy.phoenix[1] and self.rect.top <= enemy.phoenix[1] + 2 * PART_SIZE:
                if self.rect.left <= enemy.phoenix[0]:
                    self.rotate_player('r')
                else:
                    self.rotate_player('l')
                return True

            elif self.rect.left >= enemy.phoenix[0] and self.rect.left <= enemy.phoenix[0] + 2 * PART_SIZE:
                if self.rect.top <= enemy.phoenix[1]:
                    self.rotate_player('d')
                else:
                    self.rotate_player('u')
                return True
        return False

    def shoot_bullet_enemy(self):
        if self.direct_hit():
            if not self.shot_bullet:
                self.update_bullet()
        if self.bullet:
            if self.bullet.active:
                self.bullet.move(self.enemy)
                self.screen.blit(self.bullet.image, (
                    self.bullet.rect.left, self.bullet.rect.top))
            else:
                self.shot_bullet = False
