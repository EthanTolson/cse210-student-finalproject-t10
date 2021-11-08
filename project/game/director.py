import arcade
from game import constants as const

class Director(arcade.Window):
    
    def __init__(self):

        super().__init__(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, const.SCREEN_TITLE, resizable = True)

        self.all_sprites = arcade.SpriteList()


    def on_draw(self):

        arcade.start_render()
        self.all_sprites.draw()


    def setup(self):
        self.player = arcade.Sprite("cse210-student-finalproject-t10/project/game/resources/images/img.png", const.SCALING)
        self.player.center_y = const.SCREEN_HEIGHT / 2
        self.player.left = const.SCREEN_WIDTH / 2
        self.all_sprites.append(self.player)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)