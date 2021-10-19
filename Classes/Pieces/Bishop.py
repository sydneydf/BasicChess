from Classes.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, _Colour, _PieceLocation):
        super().__init__(_Colour, _PieceLocation)
        
    def __str__(self):
        return "B"

    def legalMoves(self):
        pass