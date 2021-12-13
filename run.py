from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

import pprint
from Grid import Coordinate
from Tetrimino import Tetrimino

# Encoding that will store all of your constraints
E = Encoding()

####################
#
# Propositions
#
####################

# The proposition to track the rotation state of the piece
@proposition(E)
class PieceType:

    def __init__(self, piece_type):
        self.piece_type = piece_type

    def __repr__(self):
        return f"PieceType({self.piece_type})"


O = PieceType('O')
L = PieceType('L')
I = PieceType('I')
J = PieceType('J')
S = PieceType('S')
Z = PieceType('Z')
T = PieceType('T')


class Filled(Coordinate):
    def __init__(self, place):
        self.place = place

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is occupied")


class Empty(Coordinate):
    def __init__(self, place):
        self.place = place

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is empty")


Grid = []


@constraint.implies_all(E, right=O)
@proposition(E)
class OPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        if SRS_state == 0:
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y

            Grid.append(Filled(i, j), Filled(i + 1, j), Filled(i + 1, j - 1), Filled(i, j - 1))
            # - - - -
            # - x x -
            # - x x -
            # - - - -
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"OPiece is at {self.anchor} with SRS: {self.SRS_state}"

@constraint.implies_all(E, right=L)
@proposition(E)
class LPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        if SRS_state in range(0, 4):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled())

        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"LPiece is at {self.anchor} with SRS: {self.SRS_state}"



OConfigs = {
    "first": [],
    "second": []
}

for order in OConfigs:
    for i in range(10):
        for j in range(4):

            OConfigs[order].append(OPiece(Coordinate(i, j), 0))



for order in OConfigs:
    constraint.add_exactly_one(E, *(OConfigs[order]))


def sample_theory():

    T = E.compile()

    return T


if __name__ == "__main__":

    T = sample_theory()

    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())

    pprint.pprint(T.solve())
    # print("   Solution: %s" % T.solve())




