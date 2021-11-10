import arcade

class EnemySprite(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 5

    def update(self):
        super().update()
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()

    def takeDamage(self):
        self.hitPoints -= 1