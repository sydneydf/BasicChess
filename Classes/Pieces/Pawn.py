from Classes.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, _piece_location, _colour="b"):
        super().__init__(_piece_location, _colour)
        self.hasMoved = False

    def __str__(self):
        return self.colour + "P"

    # Custom Method for Pawn
    def get_direction(self):

        # Special Moveset we just override the parent func
        direction = 0
        if self.colour == "w":
            direction = 1
        else:
            direction = -1

        return direction
