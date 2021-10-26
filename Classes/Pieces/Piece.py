from string import ascii_lowercase


class Piece:
    def __init__(self, _pieceLocation, _team="b"):  # _team or color, default to black
        # self.type = _PieceID  # Rook, Horse, Bishop, Queen, King or Pawn
        self.currentLocation = _pieceLocation  # Do we need this?? We could use this to calculate post of legal moves

        self.colour = _team  # White or Black, White always goes first

        self.uncheckedTupleMoves = []  # TODO: THIS IS DIFFERENT FOR EVERY CHILD CLASS, MAY NOT WORK
        self.isAlive = True

    # @staticmethod
    # def makePiece(_pieceStr, _pieceLocation):
    #     pass

    # parse current location into ints that we can check legal moves
    def parseLocation(self):
        xString, yString = self.currentLocation
        yInt = int(yString)
        # add one to xInt so it corresponds to alphabet if it wasn't indexed to zero
        # example: d would return 4 instead of 3
        xInt = (ascii_lowercase.find(xString)) + 1
        # Returns tuple so we unpack tuple on methodCall
        return xInt, yInt

    # technically static but kinds belongs to Piece class
    # We are trying out pythons type hinting here
    # TODO: add type hinting for methods, Paramater types and then arrow returns. Makes it more clearer
    def returnLetterNumCord(self, _xInt: int, _yInt: int) -> tuple[str, int]:
        xLetter = ascii_lowercase[(_xInt - 1)]
        return xLetter, _yInt

    def linearSlides(self):
        xInt, yInt = self.parseLocation()
        # 2 checks, Horizontal and vertical
        intTupleMoves = [zip(range(xInt + 1, 9), [yInt] * 8),  # Up
                         zip(range(xInt - 1, 0, -1), [yInt] * 8),  # Down
                         zip([xInt] * 8, range(xInt - 1, 0, -1)),  # Left
                         zip([xInt] * 8, range(xInt + 1, 9))  # Right
                         ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            tupleX, tupleY = intTupleMove
            parsedMoveList.append(self.returnLetterNumCord(tupleX, tupleY))

        return parsedMoveList


    def diagonalSlides(self):
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

    def otherMoves(self):
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

    def legalMoves(self):
        # add 1 to moves
        # Detect piece type and give moves accordingly
        # returns a list of possible moves e.g. ["d2", "c7"]

        pass

        # TODO: once moved then hasMoved = True, Upon move reset all colours pieces reset to false this is to stop
        # multiple moves?

        pass

    def doSomething(self):
        pass
