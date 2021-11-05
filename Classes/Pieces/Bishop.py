from Classes.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.uncheckedTupleMoves = []

    def __str__(self):
        return self.colour + "B"

    def legal_moves(self):
        return super().diagonal_slides()
