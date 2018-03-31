from src.others.move_generator import *


# This class represents all the player information (while and black)
class Player:

    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.piecesList = self.board.setupPieceBoard(color)
        # Will be used to determine whether the last move was enpassant or castling
        self.lastMoveType = None

        for piece in self.piecesList:
            if piece.value == Values.king:
                # Set king property of player for later use (castling, check and checkmate)
                self.king = piece
            elif piece.value == Values.rook:
                # Set king(H file)/queen(A file) side rook property of player for later use (castling)
                if piece.position.file == FileIndex.kH:
                    self.kingSideRook = piece
                else:
                    self.queenSideRook = piece

    def clearPlayerData(self):
        self.piecesList = []
        self.king = None
        self.kingSideRook = None
        self.kingSideRook = None

    def move(self, move):
        piece = self.board.getNonEmptyPieceOnPosition(move.fromSquare)
        return MoveGenerator.movePiece(piece, self.board, self, move.toSquare)

    def getAllPossibleTargetSquares(self, board):
        return MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, self, isCheckForCheck=False)

    def isUnderCheck(self, board, position=None):
        # A quick hack to check for new king position which is different from original king
        if not (position) and self.king:
            position = self.king.position
        # Think twice before using isCanTakeKing=True!
        return position in MoveGenerator.generatePossibleTargetSquaresForAllPieces(board, self.opponent,
                                                                                   isCheckForCheck=False,
                                                                                   isCanTakeKing=True)

    def isUnderCheckMate(self, board):
        # Make a move on a new board, piece and player (clone of current one)
        # And then check if the new player is under check or not
        newPlayer = copy.deepcopy(self)
        newPlayerOpponent = copy.deepcopy(self.opponent)
        newPlayer.opponent = newPlayerOpponent
        if newPlayer.isUnderCheck(board):
            for piece in self.piecesList:
                # Before checking for check
                # Make a move on a new board, piece (clones of current ones)
                # And then check if the new player is under check or not
                newBoard = copy.deepcopy(board)
                newPiece = copy.deepcopy(piece)
                for targetSquare in MoveGenerator.generatePossibleTargetSquares(piece, newBoard, newPlayer):
                    if MoveGenerator.movePiece(newPiece, newBoard, newPlayer, targetSquare):
                        newPiece.updatePosition(targetSquare)
                        # A quick hack to check for new king position which is different from original king
                        if newPiece.value == Values.king:
                            newKing = newPiece
                        else:
                            newKing = self.king
                        if not (newPlayer.isUnderCheck(newBoard, newKing.position)):
                            return False
            return True
        return False

    def __repr__(self):
        if self.color == Color.white:
            return "White"
        else:
            return "Black"
