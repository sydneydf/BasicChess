from Classes.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, _pieceLocation, _colour="b"):
        super().__init__(_pieceLocation, _colour)
        self.uncheckedTupleMoves = []

    def __str__(self):
        return "B"

    def legalMoves(self):
        # Min move = 1,1 max = 8,8 #Anything else is an illegal move
        xInt, yInt = self.parseLocation()  # e.g. 1, 4
        # RETURN LIST OF LEGAL MOVES

        # MY FAVOURITE PYTHON DISCOVERY
        # range function follows 2 parameters with an optional third
        # range(<startingIndex>, <stopping index>, option <steppingCount> defaulted to 1 because its optional)
        # range will then generate lists based on these cords

        # the zip function takes 2 paramaters each one would be list objects.
        # zip will match equivalent list indexes with each other and form a combination of the lists
        # AS A LIST OF TUPLES (Cords that we need)
        intTupleMoves = [zip(range(xInt + 1, 9), range(yInt + 1, 9)),  # Bottom-Right
                         zip(range(xInt + 1, 9), range(yInt - 1, 0, -1)),  # Bottom-Left
                         zip(range(xInt - 1, 0, -1), range(yInt + 1, 9)),  # Top-Right
                         zip(range(xInt - 1, 0, -1), range(yInt - 1, 0, -1))  # Top-Left
                         ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            intX, intY = intTupleMove
            parsedMoveList.append(self.returnLetterNumCord(intX, intY))

        return parsedMoveList
