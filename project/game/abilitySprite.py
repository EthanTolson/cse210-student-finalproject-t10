import arcade
import math
class AbilitySprite(arcade.Sprite):

    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.positionUsedX = None
        self.y = None
    
    def update(self):

        super().update()

        if math.sqrt((self.y - self.center_y)**2 + (self.positionUsedX - self.center_x)**2) > 300:
            self.remove_from_sprite_lists()


        
    def setPositionUsed(self, x, y):
        self.positionUsedX = x
        self.y = y

