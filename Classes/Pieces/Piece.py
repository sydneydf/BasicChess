from string import ascii_lowercase


class Piece(object):
    def __init__(self, _piece_location: str, _team: str = "b"):  # _team or color, default to black

        # currentLocation references spot on board and not spot on player's version board (Indexing from true 0)
        self.currentLocation = _piece_location
        self.colour = _team  # White or Black, White always goes first

        self.uncheckedTupleMoves = []

    # parse current location into ints that we can check legal moves
    def parse_location(self) -> tuple[int, int]:
        xString, yString = self.currentLocation
        yInt = int(yString)
        xInt = ascii_lowercase.find(xString)
        # Returns tuple so we unpack tuple on methodCall
        return xInt, yInt

    # technically static but kinds belongs to Piece class
    # We are trying out pythons type hinting here

    # returns string of X and Int of Y as Tuple
    def return_letter_numCord(self, _xInt: int, _yInt: int) -> tuple[str, int]:
        xLetter = ascii_lowercase[_xInt]
        return xLetter, _yInt

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

    # returns list of tuple moves for infinitely moving linear pieces
    def linear_slides(self) -> list[tuple[str, int]]:
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

    # returns list of tuple moves for infinitely moving diagonal pieces
    def diagonal_slides(self) -> list[tuple[str, int]]:
        # Min move = 0,0 max = 7,7 #Anything else is an illegal move
        xInt, yInt = self.parse_location()  # e.g. 1, 4

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

    # For Interesting moves such as King and Horse preprogrammed list of tuples in respective classes
    def other_moves(self) -> list[tuple[str, int]]:
        xInt, yInt = self.parse_location()

        legalList = []

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
