from string import ascii_lowercase


class Piece(object):
    def __init__(self, _piece_location: str, _team: str = "b"):  # _team or color, default to black
        # self.type = _PieceID  # Rook, Horse, Bishop, Queen, King or Pawn
        self.currentLocation = _piece_location  # Do we need this?? We could use this to calculate post of legal moves
        # ^this references spot on board and not spot on player's version board (Indexing from true 0)
        self.colour = _team  # White or Black, White always goes first

        self.uncheckedTupleMoves = []  # TODO: THIS IS DIFFERENT FOR EVERY CHILD CLASS, MAY NOT WORK
        self.isAlive = True

    # When del <piece object> is called we pass in the newpiece that occupies that square and return that piece
    # def __del__(self, newPiece: object) -> object:
    #     return newPiece

    # parse current location into ints that we can check legal moves
    def parse_location(self) -> tuple[int, int]:
        xString, yString = self.currentLocation
        yInt = int(yString)
        # add one to xInt so it corresponds to alphabet if it wasn't indexed to zero
        # example: d would return 4 instead of 3
        xInt = ascii_lowercase.find(xString)
        # Returns tuple so we unpack tuple on methodCall
        return xInt, yInt

    # technically static but kinds belongs to Piece class
    # We are trying out pythons type hinting here
    def return_letter_numCord(self, _xInt: int, _yInt: int) -> tuple[str, int]:
        xLetter = ascii_lowercase[_xInt]
        return xLetter, _yInt

    # TODO: TRIPLE CHECK INDEXING PASSED TO MOVE FUNCS

    # MY FAVOURITE PYTHON DISCOVERY
    # range function follows 2 parameters with an optional third
    # range(<startingIndex>, <stopping index>, option <steppingCount> defaulted to 1 because its optional)
    # range will then generate lists based on these cords

    # the zip function takes 2 parameters each one would be list objects.
    # zip will match equivalent list indexes with each other and form a combination of the lists
    # AS A LIST OF TUPLES (Cords that we need)

    # ZIP Functions credit to https://codereview.stackexchange.com/questions/105273/finding-all-legal-bishop-moves
    # @User: "SuperBiasedMan"
    # Indepth learnt the usage of the setup, a very compact iteration
    def linear_slides(self) -> list[tuple[str, int]]:
        print(self.currentLocation)
        xInt, yInt = self.parse_location()
        # 2 checks, Horizontal and vertical
        # surely theres a way to put these in a pythonic way
        intTupleMoves = []
        intTupleMoves.extend(zip(range(xInt, 8), [yInt] * (7 - xInt)))  # Up
        intTupleMoves.extend(zip(range(xInt, -1, -1), [yInt] * xInt))  # Down
        intTupleMoves.extend(zip([xInt] * yInt, range(yInt, -1, -1)))  # Left
        intTupleMoves.extend(zip([xInt] * (7 - yInt), range(yInt, 8)))  # Right

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            tupleX, tupleY = intTupleMove
            parsedMoveList.append(self.return_letter_numCord(tupleX, tupleY))

        return parsedMoveList

    def diagonal_slides(self) -> list[tuple[str, int]]:
        print(self.currentLocation)
        # Min move = 1,1 max = 8,8 #Anything else is an illegal move
        xInt, yInt = self.parse_location()  # e.g. 1, 4
        # RETURN LIST OF LEGAL MOVES

        intTupleMoves = []
        intTupleMoves.extend(zip(range(xInt, 8), range(yInt, 8)))  # Bottom-Right
        intTupleMoves.extend(zip(range(xInt, 8), range(yInt, -1, -1)))  # Bottom-Left
        intTupleMoves.extend(zip(range(xInt, -1, -1), range(yInt, 8)))  # Top-Right
        intTupleMoves.extend(zip(range(xInt, -1, -1), range(yInt, -1, -1)))  # Top-Left

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            intX, intY = intTupleMove
            parsedMoveList.append(self.return_letter_numCord(intX, intY))

        return parsedMoveList

    def other_moves(self) -> list[tuple[str, int]]:
        print("Pieces current location: " + self.currentLocation)
        xInt, yInt = self.parse_location()

        legalList = []

        # will this reference to unchecked work?
        for moveTuple in self.uncheckedTupleMoves:
            unpackedX, unpackedY = moveTuple

            possibleXMove = xInt + unpackedX
            possibleYMove = yInt + unpackedY

            if possibleXMove > 7 or possibleXMove < 0:
                continue
            elif possibleYMove > 7 or possibleYMove < 0:
                continue
            else:
                legalList.append(self.return_letter_numCord(possibleXMove, possibleYMove))
        return legalList
