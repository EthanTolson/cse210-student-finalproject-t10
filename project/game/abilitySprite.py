import arcade

class AbilitySprite(arcade.Sprite):
    
    def update(self):
        super().update()

        if self.right < 0:
            self.remove_from_sprite_lists()