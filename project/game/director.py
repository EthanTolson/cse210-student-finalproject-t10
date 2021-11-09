import arcade
import math
from game import constants as const
from game import playerSprite as pS
from game import abilitySprite
from game import lastEvent


class Director(arcade.View):
    
    def __init__(self):

        super().__init__()

        self.levent = lastEvent.lastEvent(None, None)
        self.map = False
        self.background = None
        self.abilitySprites = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.abilityUsedBool = False
        self.key = None
        self.camera_sprites = arcade.Camera(self.window.width, self.window.height)
        #self.camera_gui = arcade.Camera(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)


    def on_draw(self):

        arcade.start_render()
        self.camera_sprites.use()
        arcade.draw_lrwh_rectangle_textured(0, 0, 8000, 8000, self.background)
        self.all_sprites.draw()

        if self.levent.get_x() != None:
            arcade.draw_text(self.text, self.levent.get_x(), self.levent.get_y(), arcade.color.WHITE, 20)

        if self.map:
            #arcade.draw_text("This is a place holder for the map", self.player.center_x, self.player.center_y, arcade.color.WHITE, 20, anchor_x = "center")
            arcade.draw_lrwh_rectangle_textured(self.player.center_x-250, self.player.center_y-250, 500, 500, self.map1, 0, 167)
        

    def on_update(self, delta_time: float):
        self.all_sprites.update()
        self.text = f'x' # Last click x = {self.levent.get_int_x()} y = {self.levent.get_int_y()}'
        self.player.setlastEvent(self.levent)
        self.scroll_to_player()

    def scroll_to_player(self):
        position = self.player.center_x - self.window.width / 2, \
            self.player.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, .75)

    def on_resize(self, width: int, height: int):
        self.camera_sprites.resize(int(width), int(height))
        #self.camera_gui.resize(int(width), int(height))

    def setup(self):
        self.background = arcade.load_texture(const.RESOURCE_PATH +"images/background.png")
        self.map1 = arcade.load_texture(const.RESOURCE_PATH + "images/background1.png")
        self.player = pS.playerSprite(const.RESOURCE_PATH + "images/img.png", const.SCALING/4)
        self.player.center_y = 220
        self.player.left = 220
        self.all_sprites.append(self.player)


        self.text = "If you see this something is wrong."
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == arcade.key.TAB:
            self.map = not self.map
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.Q:
            self.abilityUsedBool = not self.abilityUsedBool
            self.key = arcade.key.Q

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.TAB:
            self.map = not self.map

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:

            x = x + self.player.center_x - self.window.width/2
            y = y + self.player.center_y - self.window.height/2

            self.player.change_x = 7 * ((x- self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
            self.player.change_y = 7 * ((y- self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))

            self.levent.set_x(x)
            self.levent.set_y(y)

        if button == arcade.MOUSE_BUTTON_LEFT and self.abilityUsedBool:
            x = x + self.player.center_x - self.window.width/2
            y = y + self.player.center_y - self.window.height/2
            self.createAbility(x, y, self.key)
            self.abilityUsedBool = False
            self.key = None
    
    def createAbility(self, x, y, key = None):
        self.qAbility = abilitySprite.AbilitySprite(const.RESOURCE_PATH +"images/img.png", 1/64)
        self.qAbility.setPositionUsed(self.player.center_x, self.player.center_y)
        
        self.qAbility.center_x = self.player.center_x
        self.qAbility.center_y = self.player.center_y
        self.all_sprites.append(self.qAbility)
        self.qAbility.change_x = 5 * ((x- self.player.center_x ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))
        self.qAbility.change_y = 5 * ((y- self.player.center_y ) / math.sqrt((x-self.player.center_x)**2 + (y- self.player.center_y)**2))