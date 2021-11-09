import arcade
#from game.director import Director
from game import startScreen
from game import constants as const

def main():
    window = arcade.Window(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, const.SCREEN_TITLE, resizable = True, fullscreen= True)
    
    startgame = startScreen.StartScreen()
    window.show_view(startgame)
    arcade.run()

if __name__ == "__main__":
    main()