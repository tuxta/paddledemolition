from GameFrame import Globals
from GameFrame import RoomObject


class Paddle(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        paddle_image = self.load_image('paddle.png')
        self.set_image(paddle_image, 72, 16)

        # - Register the paddle to handle mouse events - #
        self.handle_mouse_events = True

    def step(self):
        # - Keep object in the room - #
        if self.rect.left <= 0:
            self.x = 0
        elif self.rect.right >= Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right):
        self.x = mouse_x
