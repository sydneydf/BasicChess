from Classes.Pieces.Piece import Piece


class King(Piece):
    def __init__(self, _Colour, _PieceLocation):
        super().__init__(_Colour, _PieceLocation)
        
    def __str__(self):
        return "K"

    def legalMoves(self):
        pass