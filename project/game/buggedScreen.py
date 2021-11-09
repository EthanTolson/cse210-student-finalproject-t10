import arcade
from game.startScreen import StartScreen

class buggedScreen(arcade.View):


   
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """            
        game_view = StartScreen()
        self.window.show_view(game_view)
