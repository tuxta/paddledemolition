from GameFrame import Level
from Objects import PlayButton
from Objects import QuitButton


class Title(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('Start_BG.png')

        self.add_room_object(PlayButton(self, 225, 140))
        self.add_room_object(QuitButton(self, 425, 140))
