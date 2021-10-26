from Classes.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)

    def __str__(self):
        return "R"

    def legalMoves(self):
        return self.linearSlides()
