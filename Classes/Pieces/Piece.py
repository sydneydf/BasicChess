from string import ascii_lowercase


class Piece(object):
    def __init__(self, _piece_location: str, _team: str = "b"):  # _team or color, default to black
        # self.type = _PieceID  # Rook, Horse, Bishop, Queen, King or Pawn
        self.currentLocation = _piece_location  # Do we need this?? We could use this to calculate post of legal moves

        self.colour = _team  # White or Black, White always goes first

        self.uncheckedTupleMoves = []  # TODO: THIS IS DIFFERENT FOR EVERY CHILD CLASS, MAY NOT WORK
        self.isAlive = True

    # parse current location into ints that we can check legal moves
    def parse_location(self) -> tuple[int, int]:
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
    def return_letter_numCord(self, _xInt: int, _yInt: int) -> tuple[str, int]:
        xLetter = ascii_lowercase[(_xInt - 1)]
        return xLetter, _yInt

    # TODO: TRIPLE CHECK INDEXING PASSED TO MOVE FUNCS

    # MY FAVOURITE PYTHON DISCOVERY
    # range function follows 2 parameters with an optional third
    # range(<startingIndex>, <stopping index>, option <steppingCount> defaulted to 1 because its optional)
    # range will then generate lists based on these cords

    # the zip function takes 2 paramaters each one would be list objects.
    # zip will match equivalent list indexes with each other and form a combination of the lists
    # AS A LIST OF TUPLES (Cords that we need)

    # ZIP Functions credit to https://codereview.stackexchange.com/questions/105273/finding-all-legal-bishop-moves
    # @User: "SuperBiasedMan"
    # Indepth learnt the usage of the setup, a very compact iteration
    def linear_slides(self) -> list[tuple[str, int]]:
        xInt, yInt = self.parse_location()
        # 2 checks, Horizontal and vertical
        intTupleMoves = [zip(range(xInt + 1, 9), [yInt] * 8),  # Up
                         zip(range(xInt - 1, 0, -1), [yInt] * 8),  # Down
                         zip([xInt] * 8, range(xInt - 1, 0, -1)),  # Left
                         zip([xInt] * 8, range(xInt + 1, 9))  # Right
                         ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            tupleX, tupleY = intTupleMove
            parsedMoveList.append(self.return_letter_numCord(tupleX, tupleY))

        return parsedMoveList

    def diagonal_slides(self) -> list[tuple[str, int]]:
        # Min move = 1,1 max = 8,8 #Anything else is an illegal move
        xInt, yInt = self.parse_location()  # e.g. 1, 4
        # RETURN LIST OF LEGAL MOVES

        intTupleMoves = [zip(range(xInt + 1, 9), range(yInt + 1, 9)),  # Bottom-Right
                         zip(range(xInt + 1, 9), range(yInt - 1, 0, -1)),  # Bottom-Left
                         zip(range(xInt - 1, 0, -1), range(yInt + 1, 9)),  # Top-Right
                         zip(range(xInt - 1, 0, -1), range(yInt - 1, 0, -1))  # Top-Left
                         ]

        parsedMoveList = []
        for intTupleMove in intTupleMoves:
            intX, intY = intTupleMove
            parsedMoveList.append(self.return_letter_numCord(intX, intY))

        return parsedMoveList

    def other_moves(self) -> list[tuple[str, int]]:
        xInt, yInt = self.parse_location()

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
                legalList.append(self.return_letter_numCord(possibleXMove, possibleYMove))

        return legalList

    def legal_moves(self):
        # add 1 to moves
        # Detect piece type and give moves accordingly
        # returns a list of possible moves e.g. ["d2", "c7"]

        pass

        # TODO: once moved then hasMoved = True, Upon move reset all colours pieces reset to false this is to stop
        # multiple moves?

        pass

    def doSomething(self):
        pass
