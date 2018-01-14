from GameFrame import RoomObject


class BrickHard(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        brick_image = self.load_image('hard_brick.png')
        self.broken_image = self.load_image('brick_broken.png')
        self.broken = False
        self.set_image(brick_image, 64, 32)

    def hit(self):
        if self.broken:
            return True
        else:
            self.set_image(self.broken_image, 64, 32)
            self.broken = True
            return False
