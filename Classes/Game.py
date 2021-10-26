import random
import InvalidMove
from logging import exception

# Long class imports because in different sub directories
from Classes.Pieces.Bishop import Bishop
from Classes.Pieces.King import King
from Classes.Pieces.Knight import Knight
from Classes.Pieces.Pawn import Pawn
from Classes.Pieces.Queen import Queen
from Classes.Pieces.Rook import Rook


class Game:
    # This will need adjusting, Used in Board output print

    def __init__(self):
        self.board = {  # "   1  2  3  4  5  6  7  8"
            "a": [" "] * 8,  # "--------------------------"
            "b": [" "] * 8,  # "a|wR|wN|wB|wQ|wK|wB|wN|wR|"
            "c": [" "] * 8,  # "-------------------------"
            "d": [" "] * 8,  # "b|wP|wP|wP|wP|wP|wP|wP|wP|"
            "e": [" "] * 8,  # "--------------------------"
            "f": [" "] * 8,
            "g": [" "] * 8,
            "h": [" "] * 8,
            # Declaring empty boards
        }
        # self.horizontalLen = 19
        self.InitGame()

    def reset_board(self):
        teams = ["w", "b"]

        # Init Pawns
        for i in range(1, 9):
            self.board["b"][i] = Pawn(f"b{i}", teams[0])
            self.board["g"][i] = Pawn(f"b{i}", teams[1])

        backLinePlace = {"R": [1, 8], "N": [2, 7], "B": [3, 6], "Q": [4], "K": [5]}

        # First time using enumerate, A very "Pythonic way to loop"
        # enumerate loops return 2 loop variables:
        # count - current count of loop
        # value - current value at the current iteration of the loop

        # makes it so we dont have to have a counter declared outside and constantly update it
        # for count, team in enumerate(teams):

        # TODO: NEED TO CONSOLIDATE THIS CODE
        for pos in backLinePlace["R"]:
            self.board["a"][pos] = Rook(f"a{pos}", "w")
            self.board["h"][pos] = Rook(f"h{pos}", "b")

        for pos in backLinePlace["N"]:
            self.board["a"][pos] = Knight(f"a{pos}", "w")
            self.board["h"][pos] = Knight(f"h{pos}", "b")

        for pos in backLinePlace["B"]:
            self.board["a"][pos] = Bishop(f"a{pos}", "w")
            self.board["h"][pos] = Bishop(f"h{pos}", "b")

        self.board["a"][backLinePlace['Q'][0]] = Queen(f"a{backLinePlace['Q'][0]}", "w")
        self.board["h"][backLinePlace['Q'][0]] = Queen(f"a{backLinePlace['Q'][0]}", "b")

        self.board["a"][backLinePlace['K'][0]] = King(f"a{backLinePlace['K'][0]}", "w")
        self.board["h"][backLinePlace['K'][0]] = King(f"a{backLinePlace['K'][0]}", "b")

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
            if resignationPrompt != "":
                end = True

