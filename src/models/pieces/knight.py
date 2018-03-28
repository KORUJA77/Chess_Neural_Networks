from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the knight logic
class Knight(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.value = Values.knight

        # Knight directions
        self.directionsList.append((1, 2))
        self.directionsList.append((2, 1))

        self.directionsList.append((-1, 2))
        self.directionsList.append((-2, 1))

        self.directionsList.append((1, -2))
        self.directionsList.append((2, -1))

        self.directionsList.append((-1, -2))
        self.directionsList.append((-2, -1))

    def canMove(self, board, toSquare):
        move = EvaluationMove(self.position, toSquare)

        return Utility.isMoveInCorrectDirection(move, self.directionsList) \
               and board.checkIfSquareIsNotNil(toSquare) \
               and board.checkForClearPath(move)
