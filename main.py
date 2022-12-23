from game import Game
from config import GAME_TITLE, GAME_FRAMERATE, SCREEN_WIDTH, SCREEN_HEIGHT


def main() -> None:
    game = Game(window_size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                game_title=GAME_TITLE,
                framerate=GAME_FRAMERATE)
    game.run()


if __name__ == "__main__":
    main()
