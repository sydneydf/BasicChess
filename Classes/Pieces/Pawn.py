from Classes.Pieces.Piece import Piece

s


class Pawn(Piece):
    def __init__(self, _piece_location, _colour="b"):
        super().__init__(_piece_location, _colour)
        self.firstMove = True

    def __str__(self):
        return self.colour + "P"

    def checkFowardAttack(self):
        pass

    def legal_moves(self):
        # TODO: CANNOT TAKE PIECES IN FRONT
        # Special Moveset we just override the parent func

        xInt, yInt = self.parse_location()

        possibleMoves = []
        direction = 0
        if self.colour == "w":
            direction = 1
        else:
            direction = -1

        possibleMoves.append(self.return_letter_numCord((xInt + direction), yInt))

        if self.firstMove:
            possibleMoves.append(self.return_letter_numCord((xInt + (direction * 2)), yInt))
            # list of legal moves is +1 and +2 or -1 -2 respectively. (LETTER)

        return possibleMoves
