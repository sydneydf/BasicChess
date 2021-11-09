from Classes.Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        # TODO: INDEXING IS OFF?
        # TODO: OR LOCATION IS OFF?
        # TODO: Main thinking = Works first time but then
        #  second move always fucks up? y is off by one somewhere

        self.uncheckedTupleMoves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __str__(self):
        return self.colour + "N"

    def legal_moves(self):
        return super().other_moves()
