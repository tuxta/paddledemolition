from GameFrame import RoomObject
import pygame


class PressToStart(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        start_image = self.load_image('press_to_start.png')
        self.set_image(start_image, 400, 100)

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            self.y = -400
