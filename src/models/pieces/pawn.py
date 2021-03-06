from src.models.pieces.piece import *
from src.others.constants import *


# This class handles all the pawn logic
class Pawn(Piece):

    def __init__(self, position, color, strategy):
        super().__init__(position, color, strategy)
        self.value = Values.pawn

        # Symbol
        if color == Color.white:
            self.symbol = Symbols.white_pawn
            self.fenSymbol = FENSymbols.white_pawn
        else:
            self.symbol = Symbols.black_pawn
            self.fenSymbol = FENSymbols.black_pawn

        # Pawn directions

        # The method pawnMoveDirection(number) determines the DIRECTION according to COLOR
        self.directionsList.append((0, self.pawnMoveDirection(1)))
        self.directionsList.append((0, self.pawnMoveDirection(2)))

        self.directionsList.append((-1, self.pawnMoveDirection(1)))
        self.directionsList.append((1, self.pawnMoveDirection(1)))

    def canMovePiece(self, board, toSquare, player=None, isCheckForCastling=True):

        result = False
        enpassantMoveResult = False
        targetPiece = board.getPieceOnPosition(toSquare)
        # Simple 1 step or 2 step moves
        if board.checkIfSquareIsEmpty(toSquare):
            enpassantPiece = board.getPieceOnPosition(toSquare - (0, self.pawnMoveDirection(1)))
            if Utility.getFileAndRankAdvance(Move(self.position, toSquare)) == self.directionsList[0]:
                result = True
            elif Utility.getFileAndRankAdvance(Move(self.position, toSquare)) == self.directionsList[1] \
                    and self.hasMoved == False:
                result = True
            #######################################################
            # Start of enpassant case (if enpassant piece exists) #
            #######################################################
            elif enpassantPiece \
                    and enpassantPiece == board.movedPawn \
                    and not (enpassantPiece.color == self.color):
                fileAndRankAdvance = Utility.getFileAndRankAdvance(
                    Move(self.position, toSquare))
                if fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]:
                    result = True
                    enpassantMoveResult = True
            #####################################################
            # End of enpassant case (if enpassant piece exists) #
            #####################################################
        # Simple capture (works only if target piece exists and is of opposite color)
        elif targetPiece and not (targetPiece.color == self.color):
            fileAndRankAdvance = Utility.getFileAndRankAdvance(Move(self.position, toSquare))
            result = fileAndRankAdvance == self.directionsList[2] or fileAndRankAdvance == self.directionsList[3]

        result = result and super().canMovePiece(board, toSquare)

        if result:
            if enpassantMoveResult:
                player.lastMoveType = MoveType.enpassant
            else:
                player.lastMoveType = MoveType.normal

        return result

    def pawnMoveDirection(self, number):
        return self.color * number
