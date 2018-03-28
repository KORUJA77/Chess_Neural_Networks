from src.others.utility import *


# This class handles all the piece-centric logic
class Piece:

    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.hasMoved = False
        self.captured = False
        self.directionsList = []
        self.id = (position.rank * 10) + position.file

    def updatePosition(self, toSquare):
        self.position = toSquare
        self.hasMoved = True

    def __repr__(self):
        return "{} at {}".format(self.symbol, self.position)

    def canMove(self, board, toSquare):
        move = EvaluationMove(self.position, toSquare)

        return Utility.isMoveInCorrectDirection(move, self.directionsList) \
               and board.checkIfSquareIsNotNil(toSquare) \
               and board.checkIfEmptyOrEnemyPieceExists(self.color, toSquare) \
               and board.checkForClearPath(move)


class EmptyPiece:
    def __init__(self):
        pass
