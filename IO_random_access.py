from string import ascii_lowercase


# TODO: USING string ascii lowercase + 1 for help refinding x
# for example
class Board_Writer:
    def __init__(self, _board):
        # Maybe ask Sandar how we can have a object variable that will work like this instead of having to call it as
        # its accessesd inside the function with the "With statement"
        # self.file = open("IO_board_state.txt", mode="w+")
        self.fName = "IO_board_state.txt"
        self.init_write(_board)

    # board should be max of 128 characters long, each piece is 2 blocks
    # All in one function to literally overwrite the board each time.
    # probably not efficient but saves time :P
    # Big Brian strats
    def init_write(self, _board):
        file = open(self.fName, mode="w+")
        with file:
            # index*2 to write in proper place
            offset = 0
            for Ylist in _board.values():
                for Yvalue in Ylist:
                    file.seek(offset)
                    file.write(str(Yvalue))
                    offset += 2
        file.close()

    # if castled then call 2 times
    def update_piece(self, piece2write: str, _from: int, _to: int):
        """
        :param piece2write: string representation of piece to write
        :param _from: start square
        :param _to: where the piece has moved to
        :return: void (Update of file)
        """
        file = open(self.fName, mode="r+")
        with file:
            # index*2 to write in proper place
            file.seek(_from)
            file.write('  ')
            file.seek(_to)
            file.write(piece2write)
        file.close()
