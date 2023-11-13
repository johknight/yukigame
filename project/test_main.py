import unittest

from main import Player, Enemy, Bullet

class TestGame(unittest.TestCase):

    def test_player_initialization(self):
        player = Player(r'project/assets/pixil-frame-0.png', 100, 100, 10)
        self.assertEqual(player.rect.center, (100, 100))
        self.assertEqual(player.speed, 10)

if __name__ == '__main__':
    unittest.main()

