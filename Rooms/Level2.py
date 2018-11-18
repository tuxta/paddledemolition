import pygame
from GameFrame import Globals
from GameFrame import Level
from Objects import *


class Level2(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        pygame.mouse.set_visible(False)

        # - Set Background image - #
        self.set_background_image('space_background.jpg')

        # - Add Bricks - #
        offset_x, offset_y = 15, 15
        self.brick_count = 0

        brick_layout = [
            'hbhbsbsbhbhb',
            'bhbhbhbhbhbh',
            'hbhbhbhbhbhb',
            'bhbhshbsbhbh'
        ]

        for i in range(4):
            for j in range(12):
                if brick_layout[i][j] == 'b':
                    self.add_room_object(Brick(self, j*64+offset_x, i*32+offset_y))
                elif brick_layout[i][j] == 'h':
                    self.add_room_object(BrickHard(self, j*64+offset_x, i*32+offset_y))
                elif brick_layout[i][j] == 's':
                    self.add_room_object(SpeedBrick(self, j*64+offset_x, i*32+offset_y))
                self.brick_count += 1

        # - Add Start Text - #
        self.start_text = PressToStart(self, 200, 300)
        self.add_room_object(self.start_text)

        # - Add Paddle - #
        self.add_room_object(Paddle(self, Globals.SCREEN_WIDTH / 2, Globals.SCREEN_HEIGHT - 45))

        # - Add ball - #
        ball = Ball(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2)
        self.add_room_object(ball)

    def out_of_bounds(self):
        self.start_text.y = 300
