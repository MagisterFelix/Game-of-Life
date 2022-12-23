from __future__ import annotations
from config import COLOR_WHITE, COLOR_GREEN


class Cell:

    __objects: dict = {}
    size: int = 16

    @classmethod
    def add(cls, x: int, y: int, is_alive: bool = False) -> None:
        cls.__objects[(x, y)] = cls.__call__(x, y, is_alive)

    @classmethod
    def get(cls, x: int, y: int) -> Cell:
        return cls.__objects.get((x, y))

    @classmethod
    def clear(cls) -> None:
        cls.__objects.clear()

    @classmethod
    def get_generation(cls) -> list:
        return [cell.is_alive for cell in cls.__objects.values()]

    @classmethod
    def set_generation(cls, generation: list) -> list:
        for cell, gen in zip(cls.__objects.values(), generation):
            if cell.is_alive != gen:
                cell.change_state()

    @classmethod
    def get_count_of_neighbors(cls, cell: Cell) -> int:
        x, y = cell.x, cell.y

        count = 0

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (i, j) == (0, 0):
                    continue

                cell = cls.get(x - i, y - j)
                if cell:
                    count += cell.is_alive

        return count

    def __init__(self, x: int, y: int, is_alive: bool) -> None:
        self.__x = x
        self.__y = y
        self.__is_alive = is_alive

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def is_alive(self) -> bool:
        return self.__is_alive

    @property
    def color(self) -> tuple[int, int, int]:
        return COLOR_GREEN if self.is_alive else COLOR_WHITE

    def change_state(self) -> None:
        self.__is_alive = not self.__is_alive
