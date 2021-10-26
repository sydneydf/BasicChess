from Classes.Pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, _colour="b"):
        super().__init__(_colour)

    def __str__(self):
        return "Q"

    def legalMoves(self):
        legalMoves = []
        legalMoves.extend(self.linearSlides())
        legalMoves.extend(self.diagonalSlides())

        return legalMoves
