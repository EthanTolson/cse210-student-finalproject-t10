import arcade
from game import constants as const
from game import playerSprite as pS
from game import lastEvent


class Director(arcade.View):
    
    def __init__(self):

        super().__init__()

        self.levent = lastEvent.lastEvent(None, None)
        self.map = False
        self.background = None
        self.all_sprites = arcade.SpriteList()

        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        #self.camera_gui = arcade.Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)


    def on_draw(self):

        arcade.start_render()
        self.camera_sprites.use()
        arcade.draw_lrwh_rectangle_textured(0,0,self.window.width, self.window.height, self.background)
        self.all_sprites.draw()

        if self.levent.get_x() != None:
            arcade.draw_text(self.text, self.levent.get_x(), self.levent.get_y(), arcade.color.WHITE, 20)

        if self.map:
            arcade.draw_text("This is a place holder for the map", self.player_u.center_x, self.player_u.center_y, arcade.color.WHITE, 20, anchor_x = "center")
        

    def on_update(self, delta_time: float):
        self.all_sprites.update()
        self.text = f'x Last click x = {self.levent.get_int_x()} y = {self.levent.get_int_y()}'
        for i in range(0, 2):
            if self.levent.get_x() != None and (self.levent.get_x() <= self.player_u.center_x + i and self.levent.get_x() \
                >= self.player_u.center_x - i) and(self.levent.get_y() <= self.player_u.center_y + i and self.levent.get_y() \
                    >= self.player_u.center_y - i):
                self.player_u.change_x = 0
                self.player_u.change_y = 0
        self.scroll_to_player()

    def scroll_to_player(self):
        position = self.player_u.center_x - self.window.width / 2, \
            self.player_u.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, .05)

    def on_resize(self, width: int, height: int):
        self.camera_sprites.resize(int(width), int(height))
        #self.camera_gui.resize(int(width), int(height))

    def setup(self):
        self.background = arcade.load_texture(const.RESOURCE_PATH +"images/background.png")

        self.player_u = arcade.Sprite(const.RESOURCE_PATH + "images/img.png", const.SCALING/4)
        self.player_u.center_y = 40
        self.player_u.left = 10
        self.all_sprites.append(self.player_u )

        self.text = "If you see this something is wrong."
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.TAB:
            self.map = not self.map
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.TAB:
            self.map = not self.map

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            #ratio = ((x- self.player_u.center_x ) /100) / ((y- self.player_u.center_y ) /100)
            # ratio = ((y- self.player_u.center_y ) /100) / ((x- self.player_u.center_x ) /100)
            # if y- self.player_u.center_y > 0:
            #     self.player_u.change_y = ratio * 10
            # else:
            #     self.player_u.change_y = -ratio * 10
            
            # if x- self.player_u.center_x > 0:
            #     self.player_u.change_x = -ratio * 10#(x- self.player_u.center_x ) /100
            # else:
            #     self.player_u.change_x = ratio * 10#(x- self.player_u.center_x ) /100
            x = x + self.player_u.center_x - self.window.width/2
            y = y + self.player_u.center_y - self.window.height/2
            self.player_u.change_x = (x- self.player_u.center_x ) /100
            self.player_u.change_y = (y- self.player_u.center_y ) /100
            self.levent.set_x(x)
            self.levent.set_y(y)