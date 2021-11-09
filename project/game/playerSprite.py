import arcade
from game import lastEvent

class playerSprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.levent = lastEvent.lastEvent(None, None)

    def update(self):

        super().update()

        for i in range(0, 2):
            if self.levent.get_x() != None and (self.levent.get_x() <= self.center_x + i and self.levent.get_x() \
                >= self.center_x - i) and(self.levent.get_y() <= self.center_y + i and self.levent.get_y() \
                    >= self.center_y - i):
                self.change_x = 0
                self.change_y = 0
    
    def getlastEvent(self, levent):
        self.levent = levent