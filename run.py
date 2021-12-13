from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

import pprint
from Grid import Coordinate
from Tetrimino import Tetrimino

# Encoding that will store all of your constraints
E = Encoding()


# The proposition to track the rotation state of the piece
@proposition(E)
class PieceType:

    # Initialize the piece's type
    def __init__(self, piece_type):
        self.piece_type = piece_type

    def __repr__(self):
        return f"PieceType({self.piece_type})"


# Create all 7 piece types
O = PieceType('O')
L = PieceType('L')
I = PieceType('I')
J = PieceType('J')
S = PieceType('S')
Z = PieceType('Z')
T = PieceType('T')

# Proposition indicating whether or not a given Coordinate is occupied by a piece
class Filled(Coordinate):
    def __init__(self, place):
        self.place = place

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is occupied")

# Proposition indicating whether or not a given Coordinate is not occupied by a piece
class Empty(Coordinate):
    def __init__(self, place):
        self.place = place

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is empty")


# Grid to track the occupied coordinates
Grid = []

# In the Encoding this object implies piece type O is active
@constraint.implies_all(E, right=O)
@proposition(E)
# This is the proposition for the O piece
class OPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state == 0:
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y

            # Append the neccessary coordinates to be filled
            Grid.append(Filled(i, j), Filled(i + 1, j), Filled(i + 1, j - 1), Filled(i, j - 1))
            # - - - -
            # - x x -
            # - x x -
            # - - - -
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"OPiece is at {self.anchor} with SRS: {self.SRS_state}"

# In the Encoding this object implies piece type L is active
@constraint.implies_all(E, right=L)
@proposition(E)
# This is the proposition for the L piece
class LPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor

        # Check valid SRS states
        if SRS_state in range(0, 4):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y

            # Check for each SRS state
            if SRS_state == 0:
                # Append the neccessary coordinates to be filled
                Grid.append(Filled(i, j), Filled(i, j-1), Filled(i-1, j-1), Filled(i-2, j-1))
            # - - - -
            # - - x -
            # x x x -
            # - - - -
            
            if SRS_state == 1:
                # Append the neccessary coordinates to be filled
                Grid.append(Filled(i, j), Filled(i-1, j), Filled(i-1, j-2), Filled(i-1, j-3))
            # - x - -
            # - x - -
            # - x x -
            # - - - -

            if SRS_state == 2:
                # Append the neccessary coordinates to be filled
                Grid.append(Filled(i, j), Filled(i, j+1), Filled(i+1, j+1), Filled(i+2, j+1))
            # - - - -
            # x x x -
            # x - - -
            # - - - -

            if SRS_state == 3:
                # Append the neccessary coordinates to be filled
                Grid.append(Filled(i, j), Filled(i+1, j), Filled(i+1, j-1), Filled(i+1, j-2))
            # - x x -
            # - - x -
            # - - x -
            # - - - -            
            
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"LPiece is at {self.anchor} with SRS: {self.SRS_state}"


# In the Encoding this object implies piece type J is active
@constraint.implies_all(E, right=J)
@proposition(E)
# This is the proposition for the J piece
class JPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state in range(0, 4):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            # Check for each SRS state
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled(i, j-1), Filled(i+1, j-1), Filled(i+2, j-1))
            # - - - -
            # - x - -
            # - x x x
            # - - - -

            if SRS_state == 1:
                Grid.append(Filled(i, j), Filled(i-1, j), Filled(i-1, j-1), Filled(i-1, j-2))
            # - x x -
            # - x - -
            # - x - -
            # - - - -
            
            if SRS_state == 2:
                Grid.append(Filled(i, j), Filled(i, j+1), Filled(i-1, j+1), Filled(i-2, j+1))
            # - - - -
            # x x x -
            # - - x -
            # - - - -
            
            if SRS_state == 3:
                Grid.append(Filled(i, j), Filled(i+1, j), Filled(i+1, j+1), Filled(i+1, j+2))
            # - - x -
            # - - x -
            # - x x -
            # - - - -

        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"JPiece is at {self.anchor} with SRS: {self.SRS_state}"


# In the Encoding this object implies piece type T is active
@constraint.implies_all(E, right=T)
@proposition(E)
# This is the proposition for the T piece
class TPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state in range(0, 4):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            # Check for each SRS state
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled(i-1, j-1), Filled(i, j-1), Filled(i+1, j-1))
            # - - x -
            # - x x x
            # - - - -
            # - - - -
            
            if SRS_state == 1:
                Grid.append(Filled(i, j), Filled(i-1, j+1), Filled(i-1, j), Filled(i-1, j-1))
            # - - x -
            # - - x x
            # - - x -
            # - - - -
            
            if SRS_state == 2:
                Grid.append(Filled(i, j), Filled(i+1, j+1), Filled(i, j+1), Filled(i-1, j+1))
            # - - - -
            # - x x x
            # - - x -
            # - - - -            

            if SRS_state == 3:
                Grid.append(Filled(i, j), Filled(i+1, j-1), Filled(i+1, j), Filled(i+1, j+1))
            # - - x -
            # - x x -
            # - - x -
            # - - - -
            
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"TPiece is at {self.anchor} with SRS: {self.SRS_state}"
        
@constraint.implies_all(E, right=Z)
@proposition(E)
# This is the proposition for the Z piece
class ZPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state in range(0, 2):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            # Check for each SRS state
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled(i+1, j), Filled(i+1, j-1), Filled(i+2, j-1))
            # - - - -
            # x x - -
            # - x x -
            # - - - -
            
            if SRS_state == 1:
                Grid.append(Filled(i, j), Filled(i, j-1), Filled(i-1, j-1), Filled(i-1, j-2))
            # - - x -
            # - x x -
            # - x - -
            # - - - -            
            
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"ZPiece is at {self.anchor} with SRS: {self.SRS_state}"

@constraint.implies_all(E, right=S)
@proposition(E)
# This is the proposition for the S piece
class SPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state in range(0, 2):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            # Check for each SRS state
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled(i+1, j), Filled(i-1, j-1), Filled(i, j-1))
            # - - - -
            # - x x -
            # x x - -
            # - - - -
            
            if SRS_state == 1:
                Grid.append(Filled(i, j), Filled(i, j+1), Filled(i+1, j-1), Filled(i+1, j))
            # - x - -
            # - x x -
            # - - x -
            # - - - -
            
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"SPiece is at {self.anchor} with SRS: {self.SRS_state}"


@constraint.implies_all(E, right=I)
@proposition(E)
# This is the proposition for the I piece
class IPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        # Check valid SRS states
        if SRS_state in range(0, 2):
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            # Check for each SRS state
            if SRS_state == 0:
                Grid.append(Filled(i, j), Filled(i+1, j), Filled(i+2, j), Filled(i+3, j))
            # - - - -
            # x x x x
            # - - - -
            # - - - -
            
            if SRS_state == 1:
                Grid.append(Filled(i, j), Filled(i, j-1), Filled(i, j-2), Filled(i, j-3))
            # - x - -
            # - x - -
            # - x - -
            # - x - -
            
        else:
            raise ValueError(f"Not a valid SRS state!")

    def __repr__(self):
        return f"IPiece is at {self.anchor} with SRS: {self.SRS_state}"


# The configuations of every single piece
PieceConfigs = {
    "O": [],
    "L": [],
    "J": [],
    "T": [],
    "Z": [],
    "S": [],
    "I": []

}

# Add all possible O tetrominos
for i in range(10):
    for j in range(4):
        PieceConfigs["O"].append(OPiece(Coordinate(i, j), 0))

# Add all possible L tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(4):
            PieceConfigs["L"].append(OPiece(Coordinate(i, j), 0))

# Add all possible J tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(4):
            PieceConfigs["J"].append(OPiece(Coordinate(i, j), 0))

# Add all possible T tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(4):
            PieceConfigs["T"].append(OPiece(Coordinate(i, j), 0))

# Add all possible Z tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(2):
            PieceConfigs["Z"].append(OPiece(Coordinate(i, j), 0))

# Add all possible S tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(2):
            PieceConfigs["S"].append(OPiece(Coordinate(i, j), 0))

# Add all possible I tetrominos
for i in range(10):
    for j in range(4):
        for srs in range(2):
            PieceConfigs["I"].append(OPiece(Coordinate(i, j), 0))

for order in PieceConfigs:
    constraint.add_exactly_one(E, *(PieceConfigs[order]))

# Cannot have a coordinate both filled and Empty
def notboth(coordinate):
    constraint.add(~(Filled(coordinate) & Empty(coordinate)))

def ClearBoard():
    # Setting up the board to start
    for i in range(10):
        for j in range(4):
            # All squares begin empty
            E.add_constraint(Empty)

    T = E.compile()

    return T


if __name__ == "__main__":

    T = ClearBoard()

    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())

    pprint.pprint(T.solve())
    # print("   Solution: %s" % T.solve())




