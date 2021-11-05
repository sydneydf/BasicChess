from Classes.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.hasMoved = False

    def __str__(self):
        return self.colour + "R"

    def legal_moves(self):
        return super().linear_slides()
