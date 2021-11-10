from Classes.Pieces.Piece import Piece


# Basic King move checking, No In-depth needed as of yet
class King(Piece):
    def __init__(self, _piece_location, _colour="b"):
        super().__init__(_piece_location, _colour)
        self.hasMoved = False
        self.uncheckedTupleMoves = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (1, -1)]

    def __str__(self) -> str:
        return self.colour + "K"

    def potential_moves(self)  -> list[tuple[str, int]]:
        return super().other_moves()
