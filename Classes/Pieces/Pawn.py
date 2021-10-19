from Classes.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, _Colour, _PieceLocation):
        super().__init__(_Colour, _PieceLocation)
        
    def __str__(self):
        return "P"

    def legalMoves(self):
        pass