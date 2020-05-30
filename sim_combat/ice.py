from terrain import Terrain


class Ice(Terrain):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._factor = 17

    def __str__(self):
        return "Ice: " + super().__str__()

