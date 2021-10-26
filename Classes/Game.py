import random
from Classes.Pieces import Bishop, King, Knight, Pawn, Queen, Rook
import InvalidMove
from logging import exception


class Game:
    # This will need adjusting, Used in Board output print

    def __init__(self):
        self.board = {
            "A": [" "] * 8,  # "-----------------"
            "B": [" "] * 8,  # "|R|N|B|Q|K|B|N|R|"s
            "C": [" "] * 8,  # "-----------------"
            "D": [" "] * 8,
            "E": [" "] * 8,
            "F": [" "] * 8,
            "G": [" "] * 8,
            "H": [" "] * 8,
        }
        self.whiteTeam = []
        self.blackTeam = []
        self.horizontalLen = 19
        self.InitGame()

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
    # TODO: Minimise Prints for alpha build and then add fancy prints later
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
    # def resetBoard(self):
    #     teams = ["w", "b"]
    #     backLineRows = ["a", "h"]
    #     # all moves referenced here need index adjusting - 1
    #     placement_Letters = alphabet[:8]  # Gets letters from 0 to 8
    #     # we want A and H for placing backlines
    #
    #     backLinePlace = {"R": [1, 8], "B": [2, 7], "N": [3, 6], "Q": [4], "K": [5]}
    #
    #     # TODO: Enclose in loop of colours?
    #
    #     for backLine in backLineRows:
    #         currTeam = 0
    #         currentTeam = teams[currTeam]
    #         for piece, posList in backLinePlace.items():
    #             for pos in posList:
    #                 desiredPlacement = backLine + str(pos
    #                 # TODO: Create Piece Here with desiredPlacement
    #
    #     # B And G for Pawn Placement for i in range(8): place on B and G
    #
    #     # Deprecated
    #     for i in range(8):
    #         # Assign backline
    #         self.board["A"][i] = self.board["H"][i] = backline[i]
    #
    #         # TODO: Fix potential I index here
    #         self.board["C"][i] = self.board["D"][i] = self.board["E"][i] = self.board["F"][i] = [" "]
    #         # Assign Pawns
    #         self.board["B"][i] = self.board["G"][i] = "P"

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

    def InitCastle(self):
        # if colour team king.hasCastled == False:
        # then check blank squares between
        # Long or short castle
        pass

    def InitGame(self):
        # Initiate Game here
        print("Welcome To Basic Chess!")

        # random player order
        player1 = ""
        player2 = ""
        sides = ["White", "Black"]
        if random.randint(0, 1) == 1:
            player1, player2 = sides
        else:
            player2, player1 = sides

        # Player Turn loops here
        end = False
        while not end:
            resignationPrompt = input("Press Enter to start turn, Anything else will exit!")
            if resignationPrompt != "": end = True
