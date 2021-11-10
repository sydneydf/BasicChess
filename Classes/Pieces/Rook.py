from Classes.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.hasMoved = False

    def __str__(self) -> str:
        return self.colour + "R"

    def potential_moves(self)  -> list[tuple[str, int]]:
        return super().linear_slides()
