from Classes.Pieces.Piece import Piece


# Basic King move checking, No In-depth needed as of yet
class King(Piece):
    def __init__(self, _piece_location, _colour="b"):
        super().__init__(_piece_location, _colour)
        self.castled = False
        self.hasMoved = False
        # TODO: Ask Sandar if there is a neat way to pass self.uncheckedTupleMoves to Parent function
        self.uncheckedTupleMoves = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (1, -1)]

    def __str__(self):
        return self.colour + "K"

    def legal_moves(self):
        return super().other_moves()
