import arcade
from game.startScreen import StartScreen
from game.director import Director
from game import constants as const

def main():


    window = arcade.Window(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, const.SCREEN_TITLE, resizable = True, fullscreen= True)
    startgame = StartScreen()
    window.show_view(startgame)
    arcade.run()

if __name__ == "__main__":
    main()