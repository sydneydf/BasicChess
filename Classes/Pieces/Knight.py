from Classes.Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.uncheckedTupleMoves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __str__(self):
        return "N"

    # TODO: WILL THIS WORK?
    def legalMoves(self):
        # Min move = 1,1 max = 8,8 #Anything else is an illegal move
        xInt, yInt = self.parseLocation()  # e.g. 1, 4
        # RETURN LIST OF LEGAL MOVES

        legalList = []

        # will this reference to unchecked work?
        for moveTuple in self.uncheckedTupleMoves:
            unpackedX, unpackedY = moveTuple

            possibleXMove = xInt + unpackedX
            possibleYMove = yInt + unpackedY

            if possibleXMove > 8 or possibleXMove < 1:
                continue
            elif possibleYMove > 8 or possibleYMove < 1:
                continue
            else:
                legalList.append(self.returnLetterNumCord(possibleXMove, possibleYMove))

        # TODO: This list only factors in out of bounds moves, Maybe this is all we need?
