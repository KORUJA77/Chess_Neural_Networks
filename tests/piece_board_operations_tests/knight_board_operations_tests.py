from tests.test_utils.test_utility import *


# This class tests if knight legal moves are blocked as intended
class KnightBoardOperationsTests(unittest.TestCase):

    def setUp(self):
        self.gameLogic = GameLogic()
        self.board = self.gameLogic.board
        self.board.setupEmptyBoard()

    # ///////////
    # // WHITE //
    # ///////////

    def testGetWhiteKnightOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.isPieceExists(Values.knight, D4)

    def testPutWhiteKnightOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.knight, D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testGetBlackKnightOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.isPieceExists(-Values.knight, D4)

    def testPutBlackKnightOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.knight, D4)
