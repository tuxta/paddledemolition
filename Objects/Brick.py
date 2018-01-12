from GameFrame import RoomObject


class Brick(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        brick_image = self.load_image('brick.png')
        self.set_image(brick_image, 64, 32)
