from Classes.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.firstMove = True

    def __str__(self):
        return "P"

    def checkFowardAttack(self):
        pass

    def legalMoves(self):
        # TODO: CANNOT TAKE PIECES IN FRONT
        # Special Moveset we just override the parent func

        xInt, yInt = self.parseLocation()

        possibleMoves = []
        direction = 0
        if self.colour == "w":
            direction = 1
        else:
            direction = -1

        possibleMoves.append(self.returnLetterNumCord((xInt + direction), yInt))

        if self.firstMove:
            possibleMoves.append(self.returnLetterNumCord((xInt + (direction * 2)), yInt))
            # list of legal moves is +1 and +2 or -1 -2 respectively. (LETTER)

        return possibleMoves
