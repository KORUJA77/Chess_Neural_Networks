from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are allowed as intended
class PawnAllowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        # These 3 methods will wipe the slate clean so we can begin anew
        self.board.setupEmptyBoard()
        self.gameLogic.whitePlayer.clearPlayerData()
        self.gameLogic.blackPlayer.clearPlayerData()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhitePawnFromA2ToA4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(A2, A4))

    def testMoveWhitePawnFromF6ToF7(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.move(Values.pawn, self.testUtility.getMove(F6, F7))

    def testMoveWhitePawnFromD2ToD3ToD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveToSquare(self.testUtility.move(Values.pawn, self.testUtility.getMove(D2, D3)),
                                           D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackPawnFromA7ToA5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(A7, A5))

    def testMoveBlackPawnFromF7ToF6(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.move(-Values.pawn, self.testUtility.getMove(F7, F6))

    def testMoveBlackPawnFromD7ToD6ToD5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveToSquare(self.testUtility.move(-Values.pawn, self.testUtility.getMove(D7, D6)),
                                           D5)
