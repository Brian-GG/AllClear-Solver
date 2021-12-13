from abc import ABC, abstractmethod

# Super class for all tetromino pieces
class Tetrimino(ABC):

    @abstractmethod
    # All pieces contain an anchor and SRS_state
    def __init__(self, anchor, SRS_state):
        pass
