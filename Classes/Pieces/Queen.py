from Classes.Pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, _piece_location, _colour="b"):
        super().__init__(_piece_location, _colour)

    def __str__(self) -> str:
        return self.colour + "Q"

    # Returns both movelists of linear and diagonal
    def potential_moves(self) -> list[tuple[str, int]]:
        legalMoves = []
        legalMoves.extend(super().linear_slides())
        legalMoves.extend(super().diagonal_slides())
        return legalMoves
