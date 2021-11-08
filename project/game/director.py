import arcade
from game import constants as const
from game import playerSprite as pS
from game import lastEvent

class Director(arcade.Window):
    
    def __init__(self):

        super().__init__(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, const.SCREEN_TITLE, resizable = True, fullscreen= True)
        
        self.levent = lastEvent.lastEvent(None, None)
        self.all_sprites = arcade.SpriteList()


    def on_draw(self):

        arcade.start_render()
        self.all_sprites.draw()
        arcade.draw_text(self.text, 60, 80, arcade.color.BLUE_VIOLET, 20)

    def on_update(self, delta_time: float):
        self.all_sprites.update()
        self.text = f'Last click x = {self.levent.get_x()} y = {self.levent.get_y()}'
        for i in range(0, 10):
            if self.levent.get_x() != None and (self.levent.get_x() <= self.player_u.center_x + i and self.levent.get_x() \
                >= self.player_u.center_x - i) and(self.levent.get_y() <= self.player_u.center_y + i and self.levent.get_y() \
                    >= self.player_u.center_y - i):
                self.player_u.change_x = 0
                self.player_u.change_y = 0
        
    def setup(self):
        for i in range(0,3):
            self.player = arcade.Sprite(const.RESOURCE_PATH + "images/img.png", const.SCALING)
            self.player.center_y = i * 300 + 200
            self.player.left = i * 300 + 100
            self.all_sprites.append(self.player)

        self.player_u = arcade.Sprite(const.RESOURCE_PATH + "images/img.png", const.SCALING/4)
        self.player_u.center_y = 40
        self.player_u.left = 10
        self.all_sprites.append(self.player_u )

        self.text = "The game has started."
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.player_u.change_x = (x- self.player_u.center_x ) /100
            self.player_u.change_y = (y- self.player_u.center_y ) /100
            self.levent.set_x(x)
            self.levent.set_y(y)