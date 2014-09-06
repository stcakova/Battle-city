import sys
import pygame
from pygame import rect
from pygame.locals import *


from constants import *
from tank import Tank
from world import World
from objects_wrapper import TankWrapper


class Game:
    start = True
    game_over = False
    multiplayer = True

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("pictures/start.png")
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)
        self.game_over_screen = pygame.image.load("pictures/game_over.png")
        self.world = World()
        self._init_players()

    def _init_players(self):
        self.player = pygame.image.load("pictures/me.png").convert_alpha()
        self.player = pygame.transform.scale(
            self.player, (PART_SIZE, PART_SIZE))

        self.object = pygame.Rect((300, 380), self.player.get_size())

        self.tank = TankWrapper([300, 380], 'r', (440, 640), "pictures/me.png")
        self.tank2 = TankWrapper(
            [580, 380], 'r', (440, 0), "pictures/player2.png")
        self.enemy_tank = TankWrapper(
            [400, 180], 'r', (0, 0), "pictures/enemy.png")
        self.enemy_tank2 = TankWrapper(
            [580, 380], 'r', (0, 0), "pictures/enemy.png")

        self.tank.enemy = (self.tank2, self.enemy_tank)
        self.tank2.enemy = (self.tank, self.enemy_tank)
        self.enemy_tank.enemy = (self.tank2, self.tank)
        self.enemy_tank2.enemy = (self.tank2, self.tank)

    def start_game(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.object.left, self.object.top = 300, 380
        elif pressed[K_DOWN]:
            self.object.left, self.object.top = 300, 440
        elif pressed[K_RIGHT]:
            self.start = False
            if self.object.top == 440:
                self.multiplayer = True
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player, (self.object.left, self.object.top))

    def _game_over(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.object.left, self.object.top = 300, 480
        elif pressed[K_DOWN]:
            self.object.left, self.object.top = 300, 550
        elif pressed[K_RIGHT] and self.object.top == 480:
            self.start = True
            self.game_over = False
            self.tank.alive = True
            self.tank2.alive = True
        elif pressed[K_RIGHT] and self.object.top == 550:
            sys.exit()

        self.screen.blit(self.game_over_screen, (0, 0))
        self.screen.blit(self.player, (self.object.left, self.object.top))

    def game_loop(self, fps):
        self.world.extract_world(self.multiplayer)
        self.multiplayer = False
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if not all((self.tank.alive, self.tank2.alive)):
                self._game_over()
            elif self.start:
                self.start_game()
            else:
                self.screen.fill((0, 0, 0))
                self.world.draw_world(self.multiplayer)
                self.tank.update_tank1()
                self.enemy_tank.update_enemy()
                self.enemy_tank2.update_enemy()
                if self.multiplayer:
                    self.tank2.update_tank2()

            self.clock.tick(fps)
            pygame.display.flip()

Game().game_loop(6)
