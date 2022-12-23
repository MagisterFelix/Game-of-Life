import pygame

from cell import Cell
from area import Area


class Game:

    def __init__(self,
                 window_size: tuple[int, int],
                 game_title: str,
                 framerate: int) -> None:
        pygame.init()
        pygame.display.set_caption(game_title)

        self.width, self.height = window_size
        self.window = pygame.display.set_mode(window_size)

        self.area = Area(self.window)

        self.framerate = framerate
        self.pause = False

    def __process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                x, y = pos_x // Cell.size, pos_y // Cell.size

                if event.button == 1:
                    Cell.get(x, y).change_state()
                elif event.button == 2:
                    self.area.generate_cells(random=False)
                elif event.button == 3:
                    self.area.generate_cells()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause
                elif event.key == pygame.K_LEFT:
                    self.area.prev_generation()
                elif event.key == pygame.K_RIGHT:
                    self.area.next_generation()

    def run(self) -> None:
        self.running = True

        clock = pygame.time.Clock()

        while self.running:
            self.area.draw()
            if not self.pause:
                self.area.tick()

            self.__process_events()

            clock.tick(self.framerate)

        pygame.quit()
