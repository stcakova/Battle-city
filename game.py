import sys
import pygame
from pygame import rect
from pygame.locals import *


from constants import *
from tank import Tank
from world import World


class Game:
    start = True
    game_over = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.player = pygame.image.load("pictures/me.png").convert_alpha()
        self.player = pygame.transform.scale(
            self.player, (PART_SIZE, PART_SIZE))
        self.object = pygame.Rect((300, 380), self.player.get_size())
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("pictures/start.png")
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)
        self.game_over_screen = pygame.image.load("pictures/game_over.png")
        self.tank = Tank(self.player, self.object, 'r')
        self.direction = 'r'

    def start_game(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.object.left, self.object.top = 300, 380
        elif pressed[K_DOWN]:
            self.object.left, self.object.top = 300, 440
        elif pressed[K_RIGHT] and self.object.top == 380:
            self.start = False
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
        elif pressed[K_RIGHT] and self.object.top == 550:
            sys.exit()
        self.screen.blit(self.game_over_screen, (0, 0))
        self.screen.blit(self.player, (self.object.left, self.object.top))

    def game_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.game_over:
                self._game_over()
            elif self.start:
                self.start_game()
            else:
                self.screen.fill((0, 0, 0))
                World().draw_world()
                self.tank.move()
            self.clock.tick(60)
            pygame.display.flip()
Game().game_loop()
