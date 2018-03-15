from src.models.game_logic import *
from tests.test_utils.test_constants import *
from tests.test_utils.test_utility import *


# This class tests if player logic is working properly
class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.whitePlayer = self.gameLogic.whitePlayer
        self.blackPlayer = self.gameLogic.blackPlayer
        self.testUtility = TestUtility(self.board)

    def testMovePiece(self):
        # Move white knight on B1 to C3
        self.move(B1, C3)
        # Move black knight on B8 to A6
        self.move(G8, F6)

    def testSetKing(self):
        self.assertTrue(self.whitePlayer.king == self.board.getPieceOnPosition(E1))
        self.assertTrue(self.blackPlayer.king == self.board.getPieceOnPosition(E8))

    def setKingSideRook(self, rook):
        self.assertTrue(self.whitePlayer.kingSideRook == self.board.getPieceOnPosition(H1))
        self.assertTrue(self.blackPlayer.kingSideRook == self.board.getPieceOnPosition(H8))

    def setQueenSideRook(self, rook):
        self.assertTrue(self.whitePlayer.queenSideRook == self.board.getPieceOnPosition(A1))
        self.assertTrue(self.blackPlayer.queenSideRook == self.board.getPieceOnPosition(A8))

    def testgetAllPossibleTargetSquares(self):
        self.testUtility.checkEqualMoves(self.whitePlayer.getAllPossibleTargetSquares(),
                                         [A3, B3, C3, D3, E3, F3, G3, H3,
                                          A4, B4, C4, D4, E4, F4, G4, H4,
                                          A3, C3, F3, H3])

        self.gameLogic.changeTurn()

        self.testUtility.checkEqualMoves(self.blackPlayer.getAllPossibleTargetSquares(),
                                         [A6, B6, C6, D6, E6, F6, G6, H6,
                                          A5, B5, C5, D5, E5, F5, G5, H5,
                                          A6, C6, F6, H6])

    def testIsUnderCheck(self):
        # First see if white king is not under check
        self.assertTrue(self.whitePlayer.isUnderCheck() == False)
        # Perform fool's mate on white
        self.getCheckOnWhite()
        # Change player turn to see black's moves
        self.gameLogic.changeTurn()
        # Now check if white king is under check
        self.assertTrue(self.whitePlayer.isUnderCheck() == True)

    def testIsUnderCheckMate(self):
        # First see if white king is not under checkmate
        self.assertTrue(self.whitePlayer.isUnderCheckMate() == False)
        # Perform fool's mate on white
        self.performFoolsMateOnWhite()
        # Change player turn to see black's moves
        self.gameLogic.changeTurn()
        # Now check if white king is under checkmate
        self.assertTrue(self.whitePlayer.isUnderCheckMate() == True)

    def testTryToMoveWhileInCheck(self):
        # 1. f3 e5
        # 2. g4 Qh4#
        # 3. a3 will fail
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white pawn on G2 to G4
        self.assertTrue(self.move(G2, G4))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))
        # Move white pawn on A2 to A3
        self.assertTrue(self.move(A2, A3) == False)

    def testBlockWhileInCheck(self):
        # 1. f3 e5
        # 2. g1 -> h3 Qh4#
        # 3. g3 will pass
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white knight on G1 to H3
        self.assertTrue(self.move(G1, H3))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))
        # Move white pawn on G2 to G3
        self.assertTrue(self.move(G2, G3))

    def move(self, fromSquare, toSquare):
        piece = self.board.getPieceOnPosition(fromSquare)
        self.gameLogic.movePiece(EvaluationMove(piece.position, toSquare))
        return piece.position == toSquare

    def getCheckOnWhite(self):
        # 1. f3 e5
        # 2. g1 -> h3 Qh4#
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white knight on G1 to H3
        self.assertTrue(self.move(G1, H3))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))

    def performFoolsMateOnWhite(self):
        # 1. f3 e5
        # 2. g4 Qh4#
        # Move white pawn on F2 to F3
        self.assertTrue(self.move(F2, F3))
        # Move black pawn on E7 to E5
        self.assertTrue(self.move(E7, E5))
        # Move white pawn on G2 to G4
        self.assertTrue(self.move(G2, G4))
        # Move black queen on D8 to H4
        self.assertTrue(self.move(D8, H4))


if __name__ == '__main__':
    unittest.main()
