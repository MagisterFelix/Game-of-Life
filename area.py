from random import randint

import pygame

from config import COLOR_WHITE, COLOR_BLACK
from cell import Cell


class Area:

    def __init__(self, surface: pygame.Surface) -> None:
        self.surface = surface
        self.surface.fill(COLOR_WHITE)

        self.width = self.surface.get_width() // Cell.size
        self.height = self.surface.get_height() // Cell.size

        self.current_generation = 0
        self.generations = []
        self.generate_cells()

        self.draw()

    def generate_cells(self, random: bool = True) -> None:
        self.generations.clear()
        Cell.clear()

        for x in range(self.width):
            for y in range(self.height):
                Cell.add(x, y, bool(randint(0, 1)) if random else False)

        self.generations.append(Cell.get_generation())

    def tick(self) -> None:
        to_update = set()

        for x in range(self.width):
            for y in range(self.height):
                cell = Cell.get(x, y)
                count = Cell.get_count_of_neighbors(cell)

                if (cell.is_alive and (count < 2 or count > 3)) or \
                        (not cell.is_alive and count == 3):
                    to_update.add(cell)

        for cell in to_update:
            cell.change_state()

        self.current_generation += 1
        self.generations.append(Cell.get_generation())

    def prev_generation(self) -> None:
        if self.current_generation != 0:
            self.current_generation -= 1
            Cell.set_generation(self.generations[self.current_generation])

    def next_generation(self) -> None:
        if self.current_generation == len(self.generations) - 1:
            self.tick()
        else:
            self.current_generation += 1
            Cell.set_generation(self.generations[self.current_generation])

    def draw(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                obj = Cell.get(x, y)

                rect = pygame.Rect(x * Cell.size, y * Cell.size,
                                   Cell.size, Cell.size)
                pygame.draw.rect(self.surface, obj.color, rect)
                pygame.draw.rect(self.surface, COLOR_BLACK, rect, 1)

        pygame.display.update()
