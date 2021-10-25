from Classes.Pieces.Piece import Piece

#Basic King move checking, No In-depth needed as of yet
class King(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.castled = False
        self.uncheckedTupleMoves = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (1, -1)]

    def __str__(self):
        return "K"

    def legalMoves(self):
        xInt, yInt = self.parseLocation()

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
