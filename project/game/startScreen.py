import arcade

class StartScreen(arcade.View):

    def on_show(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Enter's Game! I hope that you enjoy playing.", self.window.width / 2, self.window.height / 2,
                         arcade.color.ARMY_GREEN, font_size=50, anchor_x="center")
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        if _button == arcade.MOUSE_BUTTON_LEFT:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
