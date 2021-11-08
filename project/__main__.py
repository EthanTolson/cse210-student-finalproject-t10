import arcade
from game.director import Director

def main():
    app = Director()
    app.setup()
    arcade.run()

if __name__ == "__main__":
    main()