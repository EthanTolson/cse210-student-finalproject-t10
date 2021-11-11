import arcade
from game import constants as const
from game import director

class StartScreen(arcade.View):

  
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Enter's Game! I hope that you enjoy playing.", self.window.width / 2, self.window.height / 2,
            arcade.color.GREEN, font_size=50, anchor_x="center")

        arcade.draw_text("Controls:", self.window.width / 2 , self.window.height / 2 - 60, 
            arcade.color.PURPLE, font_size=40, anchor_x="center")

        arcade.draw_text("Right Click: move your character to the click.\nQ + Left Click : Ability 1\nTAB(Hold): Map.\nESC = Quit\nF: Toggle Fullscreen", self.window.width / 2 , self.window.height / 2 - 110, 
            arcade.color.PURPLE, font_size=30, anchor_x="center", multiline=True, width = 600)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        if _button == arcade.MOUSE_BUTTON_MIDDLE:
            
            game_view = director.Director()
            game_view.setup()
            self.window.show_view(game_view)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)