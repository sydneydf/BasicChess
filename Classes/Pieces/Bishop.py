from Classes.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.uncheckedTupleMoves = []

    def __str__(self) -> str:
        return self.colour + "B"

    # returns list of diagonal moves
    def potential_moves(self)  -> list[tuple[str, int]]:
        return super().diagonal_slides()
