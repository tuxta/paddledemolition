import pygame
from GameFrame import Globals
from GameFrame import Level
from Objects import *


class BreakOut(Level):

    def __init__(self, screen):
        Level.__init__(self, screen)

        pygame.mouse.set_visible(False)

        # - Set Background image - #
        self.set_background_image('space_background.jpg')

        # - Add Paddle - #
        self.add_room_object(Paddle(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT-45))

        # - Add Bricks - #
        offset_x, offset_y = 15, 15
        self.brick_count = 0
        for i in range(12):
            for j in range(4):
                self.add_room_object(Brick(self, i*64+offset_x, j*32+offset_y))
                self.brick_count += 1

        # - Add Start Text - #
        self.start_text = PressToStart(self, 200, 300)
        self.add_room_object(self.start_text)

        # - Add ball - #
        ball = Ball(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2)
        self.add_room_object(ball)

    def out_of_bounds(self):
        self.start_text.y = 300
