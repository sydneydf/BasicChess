class Piece:
    def __init__(self, _Colour, _PieceLocation):
        self.colour = _Colour  # White or Black, White always goes first
        # self.type = _PieceID  # Rook, Horse, Bishop, Queen, King or Pawn
        self.currentLocation = _PieceLocation  # Do we need this?? We could use this to calculate post of legal moves

    def legalMoves(self):
        # add 1 to moves
        # Detect piece type and give moves accordingly
        # returns a list of possible moves e.g. ["d2", "c7"]

        # TODO: once moved then hasMoved = True, Upon move reset all colours pieces reset to false this is to stop
        # multiple moves?

        pass

    def doSomething(self):
        pass
