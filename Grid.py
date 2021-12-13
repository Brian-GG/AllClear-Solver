class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def x(self) -> int:
        return self.x()

    def y(self) -> int:
        return self.y()

    def set(self, other) -> None:
        if type(other) == Coordinate:
            self.x = other.x
            self.y = other.y

        else:
            raise AttributeError("That is not a coordinate")
