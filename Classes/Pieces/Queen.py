from Classes.Pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, _colour="b"):
        super().__init__(_colour)

    def __str__(self):
        return "Q"

    def legalMoves(self):
        xInt, yInt = self.parseLocation()

        intTupleMoves = [  # Horizontal and vertical
            zip(range(xInt + 1, 9), yInt),  # Up
            zip(range(xInt - 1, 0, -1), yInt),  # Down
            zip(xInt, range(xInt - 1, 0, -1)),  # Left
            zip(xInt, range(xInt + 1, 9)),  # Right

            # Diagonal Moves
            zip(range(xInt + 1, 9), range(yInt + 1, 9)),  # Bottom-Right
            zip(range(xInt + 1, 9), range(yInt - 1, 0, -1)),  # Bottom-Left
            zip(range(xInt - 1, 0, -1), range(yInt + 1, 9)),  # Top-Right
            zip(range(xInt - 1, 0, -1), range(yInt - 1, 0, -1))  # Top-Left
        ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            intX, intY = intTupleMove
            parsedMoveList.append(self.returnLetterNumCord(intX, intY))

        return parsedMoveList
