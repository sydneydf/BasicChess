from Classes.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)

    def __str__(self):
        return "R"

    def legalMoves(self):
        xInt, yInt = self.parseLocation()
        # 2 checks, Horizontal and vertical
        intTupleMoves = [zip(range(xInt + 1, 9), yInt),  # Up
                         zip(range(xInt - 1, 0, -1), yInt),  # Down
                         zip(xInt, range(xInt - 1, 0, -1)),  # Left
                         zip(xInt, range(xInt + 1, 9))  # Right
                         ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            intX, intY = intTupleMove
            parsedMoveList.append(self.returnLetterNumCord(intX, intY))

        return parsedMoveList
