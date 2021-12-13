from abc import ABC, abstractmethod


class Tetrimino(ABC):

    @abstractmethod
    def __init__(self, anchor, SRS_state):
        pass
