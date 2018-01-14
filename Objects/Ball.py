from GameFrame import Globals
from GameFrame import RoomObject
import random
import pygame


class Ball(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.moving = False

        image = self.load_image('ball.png')
        self.set_image(image, 16, 16)

        # -- Register to handle collisions with the Paddle and Bricks -- #
        self.register_collision_object('Paddle')
        self.register_collision_object('Brick')
        self.register_collision_object('BrickHard')
        self.register_collision_object('SpeedBrick')

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            if not self.moving:
                self.moving = True
                # - set the ball in motion - #
                self.set_direction(random.randint(225, 315), 8)

    def step(self):
        # - Keep object in the room - #
        if self.rect.left <= 0 or self.rect.right >= Globals.SCREEN_WIDTH:
            self.x = self.prev_x
            self.x_speed *= -1

        if self.rect.top <= 0:
            self.y = self.prev_y
            self.y_speed *= -1

        if self.rect.top >= Globals.SCREEN_HEIGHT:
            # - Reduce Lives - #
            Globals.LIVES -= 1
            # - Pause - #
            self.y = -32
            self.set_timer(60, self.out_of_bounds)

    def out_of_bounds(self):
        # - Reset the ball - #
        if Globals.LIVES > 0:
            self.x = Globals.SCREEN_WIDTH/2
            self.y = Globals.SCREEN_HEIGHT/2
            self.x_speed = 0
            self.y_speed = 0
            self.moving = False
            self.room.out_of_bounds()
        else:
            self.room.running = False

    def handle_collision(self, other):
        other_type = type(other).__name__
        if other_type == 'Paddle':
            self.y_speed *= -1
            paddle_pos = self.rect.centerx - other.rect.centerx
            self.x_speed += paddle_pos/4

        elif other_type == 'Brick':
            self.bounce(other)
            self.room.brick_count -= 1
            self.delete_object(other)
            if self.room.brick_count <= 0:
                self.room.running = False

        elif other_type == 'BrickHard':
            self.bounce(other)
            if other.hit():
                self.room.brick_count -= 1
                self.delete_object(other)
                if self.room.brick_count <= 0:
                    self.room.running = False

        elif other_type == 'SpeedBrick':
            self.bounce(other)
            self.delete_object(other)
            self.room.brick_count -= 1
            if self.y_speed < 0:
                self.y_speed -= 5
            else:
                self.y_speed += 5
            self.set_timer(150, self.slow_down)

    def slow_down(self):
        if self.y_speed < 0:
            self.y_speed += 5
        else:
            self.y_speed -= 5
