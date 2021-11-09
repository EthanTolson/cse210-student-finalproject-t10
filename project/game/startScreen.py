import arcade
from game import director

class StartScreen(arcade.View):

    def on_show(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Enter's Game! I hope that you enjoy playing.", self.window.width / 2, self.window.height / 2,
            arcade.color.GREEN, font_size=50, anchor_x="center")

        arcade.draw_text("Controls:", self.window.width / 2 , self.window.height / 2 - 60, 
            arcade.color.PURPLE, font_size=40, anchor_x="center")

        arcade.draw_text("Right Click: move your character to the click.\nTAB(Hold): Map.\nESC = Quit\nF: Toggle Fullscreen", self.window.width / 2 , self.window.height / 2 - 110, 
            arcade.color.PURPLE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        if _button == arcade.MOUSE_BUTTON_LEFT:
            game_view = director.Director()
            game_view.setup()
            self.window.show_view(game_view)
