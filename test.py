import unittest

from tank import *
from objects_wrapper import TankWrapper
from part import Wall, Brick


class TestBullet(unittest.TestCase):

    def setup(self):
        self.tank = Tank((300, 360), 'r', (440, 640))
        self.tank2 = Tank((400, 380), 'd', (0, 0))
        self.enemy = Tank((380, 380), 'r', (0, 0))
        self.tank.enemy = [self.enemy, self.tank2]
        self.tank2.enemy = [self.tank2, self.enemy]
        self.enemy.enemy = [self.tank, self.tank2]
        self.tank.update_bullet()
        self.tank2.update_bullet()
        self.enemy.update_bullet()

    def test_create_bullet(self):
        self.setup()
        self.assertIsInstance(self.tank.bullet, Bullet)

    def test_still_active(self):
        self.setup()
        for _ in range(3):
            self.tank.bullet.still_active(10, 0, self.tank.enemy)
        self.assertTrue(self.tank.bullet.active)

    def test_bullet_direction(self):
        self.setup()
        for _ in range(4):
            self.tank2.bullet.still_active(10, 0, self.tank2.enemy)
        self.assertEqual(self.tank2.bullet.direction, 'd')
        self.assertEqual(self.tank.bullet.direction, 'r')

    def test_bullet_active_after_tank_collision(self):
        self.setup()
        for _ in range(3):
            self.enemy.bullet.still_active(10, 0, self.enemy.enemy)
        self.assertFalse(self.enemy.bullet.active)

    def test_coordinates_after_bullet_hit(self):
        self.setup()
        self.assertEqual((self.tank.rect.left, self.tank.rect.top), (300, 360))

    def test_bullet_active_after_death(self):
        self.setup()
        self.tank.alive = False
        self.assertTrue(self.tank.bullet.active)

    def test_bullet_active_after_wall_collision(self):
        self.setup()
        for _ in range(10):
            self.tank2.bullet.still_active(10, 0, self.tank2.enemy)
        self.assertFalse(self.tank2.bullet.active)

    def test_active_bullet_after_tank_movement(self):
        self.setup()
        self.tank2.set_coordinates(
            [self.tank2.rect.left + 31, self.tank.rect.top])
        for _ in range(3):
            self.enemy.bullet.still_active(10, 0, self.enemy.enemy)
        self.assertTrue(self.enemy.bullet.active)


class TestTank(unittest.TestCase):

    def setup(self):
        self.tank = Tank((300, 360), 'r', (440, 640))
        self.tank2 = Tank((400, 380), 'd', (0, 0))
        self.enemy = Tank((380, 380), 'r', (0, 0))
        self.tank.enemy = [self.enemy, self.tank2]
        self.tank2.enemy = [self.tank2, self.enemy]
        self.enemy.enemy = [self.tank, self.tank2]
        self.tank.update_bullet()
        self.tank2.update_bullet()
        self.enemy.update_bullet()

    def test_tank_coordinates_after_wall_collision(self):
        self.setup()
        for _ in range(10):
            self.tank.valid_move(10, 0)
        self.assertEqual(self.tank.rect.right, 380)

    def test_tank_movement(self):
        self.setup()
        self.tank.valid_move(0, 10)
        self.tank.direction = 'd'
        self.tank.valid_move(10, 0)
        self.assertEqual((self.tank.rect.left, self.tank.rect.top), (310, 370))
        self.assertEqual(self.tank.direction, 'd')

    def test_tank_collision_detection(self):
        self.setup()
        self.assertFalse(self.tank.valid_move(120, 0))
        self.assertTrue(self.tank.valid_move(200, 10))

    def test_tank_coordinates_after_tank_collision(self):
        self.setup()
        for _ in range(2):
            self.tank.valid_move(0, 10)
        self.assertEqual(self.tank.rect.top, self.enemy.rect.top)

if __name__ == '__main__':
    unittest.main()
