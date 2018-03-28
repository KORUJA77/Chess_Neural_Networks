from tests.test_utils.test_utility import *


# This class tests if king legal moves are disallowed as intended
class KingDisallowMovesTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testMoveWhiteKingFromA1ToB2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(A1, C2))

    def testMoveWhiteKingFromG7ToG8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.king, self.testUtility.getMove(G7, B8))

    def testMoveWhiteKingFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.king, self.testUtility.getMove(A4, E5)),
                                      F4)

    # ///////////
    # // BLACK //
    # ///////////

    def testMoveBlackKingFromA1ToB2(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(D1, B2))

    def testMoveBlackKingFromG7ToG8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.king, self.testUtility.getMove(A7, G8))

    def testMoveBlackKingFromD4ToE5ToF4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.king, self.testUtility.getMove(A4, E5)),
                                            F4)
