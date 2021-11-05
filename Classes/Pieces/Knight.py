from Classes.Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.uncheckedTupleMoves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __str__(self):
        return self.colour + "N"

    # TODO: WILL THIS WORK?
    def legal_moves(self):
        return super().other_moves()

