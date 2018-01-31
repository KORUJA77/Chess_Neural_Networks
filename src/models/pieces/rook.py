from src.others.constants import *
from src.others.structures import *
from src.others.utility import *
from src.models.board import *
from src.models.pieces.piece import *
from src.models.pieces.strategies.unlimited_move_strategy import *

# This class handles all the rook logic
class Rook(Piece):
    
    def __init__(self,color,position,hasMoved,delegate,board):
        self.initialize(color,position,hasMoved,delegate,board)
        self.directionsList = []       
        self.symbol = Symbols.rook
        self.value = abs(Values.rook)
        
        # Rook directions
        self.directionsList.append(( 1,  0))
        self.directionsList.append(( 0,  1))
        self.directionsList.append((-1,  0))
        self.directionsList.append(( 0, -1))
        
        self.moveStrategy = UnlimitedMoveStrategy(color,self.directionsList)
    
    def moveToSquare(self,toSquare):
        return self.move(EvaluationMove(self.position,toSquare))\
        and self.board.checkForClearPath(EvaluationMove(self.position,toSquare))

    def move(self,move):
        
        result = False
        
        if fileOrRankAdvanceExclusiveCheck(EvaluationMove(move.fromSquare,move.toSquare)):            
            result = True
        
        return result
        