from tests.test_utils.test_utility import *


# This class tests if rook legal moves are disallowed as intended
class RookDisallowMovesTests(unittest.TestCase):

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

    def testfailToMoveButValidMoveOnNewBoardWhiteRookFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A1, H8))

    def testfailToMoveButValidMoveOnNewBoardWhiteRookFromH8ToC1(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMove(Values.rook, self.testUtility.getMove(H8, C1))

    def testfailToMoveButValidMoveOnNewBoardWhiteRookFromA4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.whitePlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)

    # ///////////
    # // BLACK //
    # ///////////

    def testfailToMoveButValidMoveOnNewBoardBlackRookFromA1ToH8(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A1, H8))

    def testfailToMoveButValidMoveOnNewBoardBlackRookFromH8ToC5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(H8, C5))

    def testfailToMoveButValidMoveOnNewBoardBlackRookFromA4ToD5ToF5(self):
        self.testUtility = TestUtility(self.board, self.gameLogic.blackPlayer)
        self.testUtility.failToMoveToSquare(self.testUtility.failToMove(-Values.rook, self.testUtility.getMove(A4, D5)),
                                            F5)
