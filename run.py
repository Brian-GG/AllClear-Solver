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

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is occupied")


class Empty(Coordinate):

    def __repr__(self) -> str:
        return repr(f"({self.x}, {self.y}) is empty")


@constraint.implies_all(E, right=O)
@proposition(E)
class OPiece(Tetrimino):

    def __init__(self, anchor, SRS_state):
        self.anchor = anchor
        if SRS_state == 0:
            self.SRS_state = SRS_state
            i = self.anchor.x
            j = self.anchor.y
            constraint.implies_all(Filled(i, j), Filled(i + 1, j), Filled(i + 1, j + 1), Filled(i, j + 1))

        else:
            raise ValueError(f"Not a valid SRS state!")






# class PieceConfig:
#     def __init__(self, piece_name, SRSstate) -> None:
#         self.piece_name = piece_name
#         self.SRSstate = SRSstate
#
#     def __repr__(self) -> str:
#         return f"PieceConfig({self.piece_name, self.SRSstate})"
#
# numConfigs = {
#     'I': 2,
#     'J': 4,
#     'L': 4,
#     'O': 1,
#     'S': 2,
#     'T': 4,
#     'Z': 2
# }
#
# pieceConfigs = {
#     'I': [],
#     'J': [],
#     'L': [],
#     'O': [],
#     'S': [],
#     'T': [],
#     'Z': []
# }
#
# for piece_name in pieceConfigs:
#     for i in range(pieceConfigs[piece_name]):
#         pieceConfigs[piece_name].append(PieceConfig(piece_name, i))
#
#
# for piece_name in pieceConfigs:
#     constraint.add_exactly_one(E, *(pieceConfigs[piece_name]))
#
#
#
# # The propostition to place a piece onto the board
# @proposition(E)
# class PiecePosition:
#     def __init__(self, num,  piece_name, SRSstate, x, y) -> None:
#         self.num = num
#         self.piece_name = piece_name
#         self.SRSstate = SRSstate
#         self.x = x
#         self.y = y
#
#     def __repr__(self) -> str:
#         return f"({self.piece_name, self.SRSstate, self.x, self.y})"
#
# piecePlacements = {
#     "1": {piece_name: {SRSstate: {} for SRSstate in range(numConfigs[piece_name])} for piece_name in range(pieceConfigs)},
#     "2": {piece_name: {SRSstate: {} for SRSstate in range(numConfigs[piece_name])} for piece_name in range(pieceConfigs)},
#     "3": {piece_name: {SRSstate: {} for SRSstate in range(numConfigs[piece_name])} for piece_name in range(pieceConfigs)},
#     "4": {piece_name: {SRSstate: {} for SRSstate in range(numConfigs[piece_name])} for piece_name in range(pieceConfigs)},
#     "5": {piece_name: {SRSstate: {} for SRSstate in range(numConfigs[piece_name])} for piece_name in range(pieceConfigs)}
# }
#
# piecesAtLocation = {}
#
# pieceLocationsByNum = {
#     num: [] for num in piecePlacements
# }
#
# for num in piecePlacements:
#     for piece_name in pieceConfigs:
#         for SRS in range(pieceConfigs[piece_name]):
#             for x in range(10):
#                 for y in range(20):
#                     prop = PiecePosition(num, piece_name, SRS, x, y)
#
#                     piecePlacements[num][piece_name][SRS][(x, y)] = prop
#                     pieceLocationsByNum[num].append(prop)
#
#                     if (x, y) not in piecesAtLocation:
#                         piecesAtLocation[(x, y)] = []
#                     piecesAtLocation[(x, y)].append(prop)
#
#
# @proposition(E)
# class PlaceNumber:
#     def __init__(self, num, x, y) -> None:
#         self.num = num
#         self.x = x
#         self.y = y
#
#     def __repr__(self) -> str:
#         return f"PlaceColour({self.num}, {self.x}, {self.y})"
#
# numAtLocation = {}
# for x in range(10):
#     for y in range(20):
#         numAtLocation[(x,y)] = {}
#         for num in piecePlacements:
#             prop = PlaceNumber(num, x, y)
#             numAtLocation[(x, y)][num] = prop
#
# #####################
# #
# # Constraints
# #
# #####################
#
#
# for num in piecePlacements:
#     constraint.add_exactly_one(E, *(piecePlacements[num]))
#
# def checkIfLegalPlacement(piece_name, SRSstate, x, y):
#     if piece_name is 'I':
#         if SRSstate is 0:
#             if x > 7 or x < 1:
#                 return False
#
#         if SRSstate is 1:
#             if y < 2:
#                 return False
#
#     elif piece_name is 'J':
#         if SRSstate is 0:
#             if x > 7:
#                 return False
#
#         if SRSstate is 1:
#             if x > 8 or y < 2:
#                 return False
#
#         if SRSstate is 2:
#             if x < 2 or y < 1:
#                 return False
#
#         if SRSstate is 3:
#             if x < 1:
#                 return False
#
#     elif piece_name is 'L':
#         if SRSstate is 0:
#             if x < 2:
#                 return False
#
#         if SRSstate is 1:
#             if x > 8:
#                 return False
#
#         if SRSstate is 2:
#             if x > 7 or y < 1:
#                 return False
#
#         if SRSstate is 3:
#             if x < 1 or y < 2:
#                 return False
#
#     elif piece_name is 'O':
#         if SRSstate is 0:
#             if x < 1 or y < 1:
#                 return False
#
#     elif piece_name is 'S':
#         if SRSstate is 0:
#             if x > 8 or x < 1 or y < 1:
#                 return False
#
#         if SRSstate is 1:
#             if x > 8 or y < 1:
#                 return False
#
#     elif piece_name is 'T':
#         if SRSstate is 0:
#             if x > 8 or x < 1:
#                 return False
#
#         if SRSstate is 1:
#             if x > 8  or y < 1:
#                 return False
#
#         if SRSstate is 2:
#             if x > 8 or x < 1 or y < 1:
#                 return False
#
#         if SRSstate is 3:
#             if x < 1 or y < 1:
#                 return False
#
#     elif piece_name is 'Z':
#         if SRSstate is 0:
#             if x > 8 or x < 1 or y < 1:
#                 return False
#
#         if SRSstate is 1:
#             if x < 1 or y < 1:
#                 return False
#
#     return True
#
#
# for num in piecePlacements:
#     for piece_name in range(numConfigs):
#         for SRSstate in range(numConfigs[piece_name]):
#             for x in range(10):
#                 for y in range(20):
#                     if not checkIfLegalPlacement(piece_name, SRSstate, x, y):
#                         E.add_constraint(~PiecePosition(num, piece_name, SRSstate, x, y))
#
# for x in range(10):
#     for y in range(20):
#         constraint.add_at_most_one(E, *(piecesAtLocation[(x, y)]))
#
# for num in pieceLocationsByNum:
#     constraint.add_exactly_one(E, *(pieceLocationsByNum[num]))
#
# for num in pieceLocationsByNum:
#     for var in pieceLocationsByNum[num]:
#         cVar = pieceConfigs[piecePlacements.piece_name][var.config_num]
#         E.add_constraint(var >> cVar)
#
#
#
#

def sample_theory():

    E.add_constraint()

    T = E.compile()
    return T


if __name__ == "__main__":

    T = sample_theory()

    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("Solution " % T.solve())

    # print("   Solution: %s" % T.solve())




