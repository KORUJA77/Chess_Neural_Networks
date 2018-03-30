from tests.test_utils.test_utility import *


# This class tests if pawn legal moves are blocked as intended
class PawnBoardOperationsTests(unittest.TestCase):

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

    def testGetWhitePawnOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.isPieceExists(Values.pawn, D4)

    def testPutWhitePawnOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.moveValueToSquare(Values.pawn, D4)

    # ///////////
    # // BLACK //
    # ///////////

    def testGetBlackPawnOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.isPieceExists(-Values.pawn, D4)

    def testPutBlackPawnOnD4(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.moveValueToSquare(-Values.pawn, D4)
