from string import ascii_lowercase


# TODO: USING string ascii lowercase + 1 for help refinding x
# for example
class Board_Writer:
    def __init__(self, _board):
        # Maybe ask Sandar how we can have a object variable that will work like this instead of having to call it as
        # its accessesd inside the function with the "With statement"
        # self.file = open("IO_board_state.txt", mode="w+")
        self.write_board(_board)

    # board should be max of 128 characters long, each piece is 2 blocks
    # All in one function to literally overwrite the board each time.
    # probably not efficient but saves time :P
    # Big Brian strats
    def write_board(self, _board):
        file = open("IO_board_state.txt", mode="w+")
        with file:
            # index*2 to write in proper place
            offset = 0
            for Ylist in _board.values():
                for Yvalue in Ylist:
                    file.seek(offset)
                    file.write(str(Yvalue))
                    offset += 2
        file.close()

    # move from to indexes
    # _itemsToUpdate = {'NewContents of select square': index to update}
    # def update_Board(self, _itemsToUpdate: {'str', int}):
    #     # TODO:
    #     offset = 1
    #     with self.file:
    #         for newContentKey, contentSQvalue in _itemsToUpdate.items():
    #             file.seek(contentSQvalue + offset)
    #             file.write(newContentKey)
    #         file.close()

    # TODO:  Maybe we can do dict.values to unpack our self.board board into straight values then write those
    # find letter in ascii_lowercase to get index number and maybe + 11
    # def dictIndexConverter(self):
    #     pass
