import arcade

class BossSprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 500
        self.center_x = 1000
        self.center_y = 1000

    def update(self):
        super().update()
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()
