#!/usr/bin/env python3

import unittest
from unittest.mock import Mock
import pygame

from main import Player

class TestGame(unittest.TestCase):

    def test_player_initialization(self):
        mock_image = Mock()
        mock_rect = pygame.Rect(0, 0, 20, 20)
        mock_rect.center = (100, 100)
       
        mock_image.get_rect.return_value = mock_rect

        player = Player(mock_image, 100, 100, 10)
        self.assertEqual(player.rect.center, (100, 100))
        self.assertEqual(player.speed, 10)

if __name__ == '__main__':
    unittest.main()
