from logging import exception


class Game:
    # This will need adjusting, Used in Board output print

    def __init__(self):
        self.board = {
            "A": [" "] * 8,  # "-----------------"
            "B": [" "] * 8,  # "|R|N|B|Q|K|B|N|R|"
            "C": [" "] * 8,  # "-----------------"
            "D": [" "] * 8,
            "E": [" "] * 8,
            "F": [" "] * 8,
            "G": [" "] * 8,
            "H": [" "] * 8,
        }
        self.horizontalLen = 19

    def printHorizontalCordNums(self):
        # Print Numbers for top of board
        # No Returns, just print statements
        count = 0
        print(" ", end="")
        for index in range(self.horizontalLen + 1):
            if (index == 1) | (index % 2 == 1):
                print(f" {count}", end="")
                count += 1

    def printBetweenRow(self):
        # Print between each line
        # No Returns, just print statements

        print(" ", end="")
        # do we need to print a \n here?
        for i in range(self.horizontalLen + 2):
            print("-", end="")

    # will this str dunder work like this? or will need explicit conversion
    def __str__(self):
        # No Returns, just print statements

        self.printHorizontalCordNums()
        print("\n", end="")
        self.printBetweenRow()
        for keyParent, valueParent in self.board.items():  # Iterate over each item in dictionary
            print(f"\n{keyParent}", end="")
            for value in valueParent:  # Iterate over each value in the itemParent.Value
                print("|", end="")
                print(value, end="")
            print(f"|{keyParent}")
            self.printBetweenRow()
        print("\n", end="")
        self.printHorizontalCordNums()

    def checkWin(self):
        # TODO Check if K on board less than 2, then output the colour of remaining King
        pass

    # Will this work??
    def resetBoard(self):
        backline = ["R", "N", "B", "Q", "K", "B", "N", "R"]

        for i in range(8):
            # Assign backline
            self.board["A"][i] = self.board["H"][i] = backline[i]

            # TODO: Fix potential I index here
            self.board["C"][i] = self.board["D"][i] = self.board["E"][i] = self.board["F"][i] = [" "]
            # Assign Pawns
            self.board["B"][i] = self.board["G"][i] = "P"

    def writeState2File(self):
        exception("Not implemented")
        pass

    def moveParser(self, _moveString):
        moveSplit = _moveString.split()  # "d2" turns into ["d", "2"] then maybe we capitalise D?
        # we then return cordinate or list?
        # Game Methods Here
        return moveSplit

    def makeMove(self, _moveString):
        splitMove = self.moveParser(_moveString)
        # initiate move on board
        # check if not pawn and then initiate capture method
        pass
