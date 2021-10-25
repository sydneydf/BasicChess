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
