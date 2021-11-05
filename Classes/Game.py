import random
from string import ascii_lowercase
from Classes.InvalidMove import InvalidMove

# Long class imports because in different sub directories
from Classes.Pieces.Bishop import Bishop
from Classes.Pieces.King import King
from Classes.Pieces.Knight import Knight
from Classes.Pieces.Pawn import Pawn
from Classes.Pieces.Queen import Queen
from Classes.Pieces.Rook import Rook
from Classes.Pieces.Piece import Piece


class Game:
    # This will need adjusting, Used in Board output print

    # self.board indexing in functions may cause false positives in PyCharm IDE
    def __init__(self):
        # store king states in memory for quick ref without searching
        self.kings = []
        self.board = {  # "   1  2  3  4  5  6  7  8"
            "a": ["  "] * 8,  # "--------------------------"
            "b": ["  "] * 8,  # "a|wR|wN|wB|wQ|wK|wB|wN|wR|"
            "c": ["  "] * 8,  # "-------------------------"
            "d": ["  "] * 8,  # "b|wP|wP|wP|wP|wP|wP|wP|wP|"
            "e": ["  "] * 8,  # "--------------------------"
            "f": ["  "] * 8,
            "g": ["  "] * 8,
            "h": ["  "] * 8,
            # Declaring empty boards
        }
        self.horizontalLen = 19
        self.InitGame()
        self.successfulMove = False

    def reset_board(self):

        # TODO: Will we have problems referencing these piece objects?
        # Do we have to store them in a team list instead of storing them on the self.board?

        teams = ["w", "b"]

        # Init Pawns
        for i in range(0, 8):
            self.board["b"][i] = Pawn(f"b{i}", teams[0])
            self.board["g"][i] = Pawn(f"b{i}", teams[1])

        backLinePlace = {"R": [0, 7], "N": [1, 6], "B": [2, 5], "Q": [3], "K": [4]}

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

        # HOW can we have a persistent updating reference that updates self.kings with current kings state instead of
        # straight clones? Getter Setter?

        self.kings.append(self.board["a"][4])
        self.kings.append(self.board["h"][4])

    def checkWin(self):
        # TODO Check if K on board less than 2, then output the colour of remaining King

        # can we shorten this statement?
        if len(self.kings) == 1:
            return self.kings[0]
        else:
            # no returns so game continues?
            pass

    def writeState2File(self):
        # idk if this is treated like an exception???
        raise NotImplemented()
        pass

    # this just gets proper input of a move choice
    def input_getSquare(self, msgprompt: str) -> (str, int):
        properMoveFormat = False
        xLetter = None
        yInt = None
        print(msgprompt)
        while not properMoveFormat:
            potentialMove = input("Please select a valid coordinate for this>: ")
            if len(potentialMove) == 2:

                xLetter, yString = potentialMove

                try:
                    yInt = int(yString)
                except ValueError or IndexError:
                    break

                if xLetter not in self.board.keys() or yInt not in range(1, 9):
                    break

                # If all nots fail then while loop passes
                print(f"\nInput Move Validator: Valid Cord of {xLetter} {yInt}")
                print(f"Converting move to board friendly {xLetter} {yInt - 1}\n")
                properMoveFormat = True

            else:
                print("Please Choose a proper board location")

        return xLetter, yInt - 1

    def castle_init(self, _combinedSelectCord, _combinedMoveCord):
        currXstr, currYint = _combinedSelectCord
        currYint = int(currYint)
        moveXstr, moveYint = _combinedMoveCord
        moveYint = int(moveYint)

        # False Positives
        selectedPiece: King = self.board[currXstr][currYint]
        squareToTake: Rook = self.board[moveXstr][moveYint]

        # Do not have to check distance because both pieces have to be in starting squares
        if not selectedPiece.castled == selectedPiece.hasMoved == squareToTake.hasMoved:
            # check if any squares in between
            # Start Cord and End Cord and check in between / pos and neg
            # Ok we don't need to change x cord, just either rook pos 1 or 8 and king pos 5

            # TODO: Test if break in these statements will work to return while loop move again

            if moveYint < currYint:
                for Ycheck in range(moveYint + 1, currYint):
                    if self.board[moveXstr][Ycheck] != "  ":
                        raise InvalidMove("Cannot Castle if space between is not empty")
            else:
                for Ycheck in range(currYint - 1, moveYint, -1):
                    if self.board[moveXstr][Ycheck] != "  ":
                        raise InvalidMove("Cannot Castle if space between is not empty")

            # TODO: If all checks pass then we should have this castle or swap occur here, UPDATE: PROBABLY
            selectedPiece.currentLocation = f"{moveXstr}{moveYint + 1}"
            squareToTake.currentLocation = f"{currXstr}{currYint + 1}"

            self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, squareToTake
            selectedPiece.hasMoved = squareToTake.hasMoved = True
            selectedPiece.castled = True
            return

    def same_team(self):
        pass

    def pawn_move(self, _combinedSelectCord, _combinedMoveCord):
        print(f"Parsed in Combined Selected cord: {_combinedSelectCord}")
        print(f"Parsed in Combined Move cord: {_combinedMoveCord}")

        currXstr, currYint = _combinedSelectCord
        currYint = int(currYint)

        moveXstr, moveYint = _combinedMoveCord
        moveYint = int(moveYint)

        selectedPiece: Pawn = self.board[currXstr][currYint]
        squareToTake = self.board[moveXstr][moveYint]

        legal_moves = []
        foward = selectedPiece.get_direction()

        currXint = ascii_lowercase.find(currXstr)

        # Would slim this down but we need both to be appended
        # Double Move
        if not selectedPiece.hasMoved:
            legal_moves.append((ascii_lowercase[currXint + (foward * 2)], currYint))
        # Single Move
        legal_moves.append((ascii_lowercase[currXint + foward], currYint))

        # TODO: ALot of REPEATED CODE HERE
        if currYint == 7 and isinstance(self.board[ascii_lowercase[currXint + foward]][currYint - 1], Piece):
            legal_moves.append((ascii_lowercase[currXint + foward], currYint - 1))
        elif currYint == 0 and isinstance(self.board[ascii_lowercase[currXint + foward]][currYint + 1], Piece):
            legal_moves.append((ascii_lowercase[currXint + foward], currYint + 1))
        else:
            for Ycheck in range(currYint - 1, currYint + 1, 2):
                squareCheck = self.board[moveXstr][Ycheck]
                if isinstance(squareCheck, Piece):
                    legal_moves.append((ascii_lowercase[currXint + foward], Ycheck))

        for movecord in legal_moves:
            print(f"DEBUGGING Legal move cords: {movecord[0]}, {movecord[1]}")

        if (moveXstr, moveYint) in legal_moves:
            self.king_destroyed_check(self.board[moveXstr][moveYint])
            selectedPiece.currentLocation = f"{moveXstr}{moveYint + 1}"
            selectedPiece.hasMoved = True
            print(f"Attempting to move from {currXstr}, {currYint} TO move square on {moveXstr}{moveYint}")
            self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, "  "
            return True

    def normal_move(self, _combinedSelectCord, _combinedMoveCord):
        currXstr, currYint = _combinedSelectCord
        currYint = int(currYint)

        moveXstr, moveYint = _combinedMoveCord
        moveYint = int(currYint)

        selectedPiece = self.board[currXstr][currYint]
        squareToTake = self.board[moveXstr][moveYint]

        for tupleCord in selectedPiece.legal_moves():
            if tupleCord == (moveXstr, moveYint):
                selectedPiece.currentLocation = f"{moveXstr}{moveYint + 1}"
                self.king_destroyed_check(self.board[moveXstr][moveYint])
                self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, "  "
                return
        return

    # initiate move on board
    # check if not pawn and then initiate capture method

    # This might be our longest method, we might have to break this one down alot

    # TODO Seperate move into the above funcs
    # TODO: NUMBER1 CHECK IF WE ARE REVERTING LOCATION ONLY IN GAME METHOD -1 and +1 indices etc
    def make_move(self, _colour):

        # Here we handle all move possibilities

        # MUST GET A VALID PIECE
        selectedPiece: str = "  "  # Changed after assignment
        currXstr: str = "z"  # Out of index on purpose
        currYint: int = 99
        while selectedPiece == "  ":
            # returns str, int cords
            currXstr, currYint = self.input_getSquare("Please select one of your OWN piece")
            proposedSelected = self.board[currXstr][currYint]
            if proposedSelected != "  " and proposedSelected.colour == _colour:
                selectedPiece = self.board[currXstr][currYint]
            else:
                print("Non Valid piece selected\n")
        # this is kind of useless if the above check passes

        selectedPiece: Piece

        # If selecting opponents pieces
        # if selectedPiece.colour != _colour:
        #     raise InvalidMove("Can't select enemy team colour")

        self.successfulMove = False
        while not self.successfulMove:
            try:
                moveXstr, moveYint = self.input_getSquare("Please enter a square to move to")
                moveXstr: str
                moveYint: int

                squareToTake = self.board[moveXstr][moveYint]  # Error here might be false positive

                # Illegal moves not working

                # Check for pawn moves
                if isinstance(selectedPiece, Pawn):
                    print(f"DEBUGGING: Pawn Move triggered on {moveXstr}{moveYint}")
                    if self.pawn_move(f"{currXstr}{currYint}", f"{moveXstr}{moveYint}"):
                        self.successfulMove = True

                elif squareToTake == "  ":
                    print("DEBUGGING: Empty Take Move triggered")

                    for tupleCord in selectedPiece.legal_moves():
                        if (moveXstr, moveYint) == tupleCord:
                            self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, "  "
                            self.board[moveXstr][moveYint].currentLocation = f"{moveXstr}{moveYint}"
                            self.successfulMove = True
                    break

                # Check for KING/ROOK CASTLING FIRST
                # Only King can INITIATE CASTLE
                elif isinstance(selectedPiece, King) == isinstance(squareToTake, Rook) == (
                        selectedPiece.colour == squareToTake.colour):
                    print("DEBUGGING: Castle Move triggered")
                    if self.castle_init(f"{currXstr}{currYint}", f"{moveXstr}{moveYint}"):
                        self.successfulMove = True
                    else:
                        raise InvalidMove("Could not Complete Empty move - Try moving again")
                        pass

                # Eliminate teamkill AFTER castle check
                elif selectedPiece.colour == squareToTake.colour:
                    raise InvalidMove("Cannot take own piece - choose again")
                    # break?

                else:
                    print("DEBUGGING: Normal Move triggered")
                    if self.normal_move(f"{currXstr}{currYint}", f"{moveXstr}{moveYint}"):
                        self.successfulMove = True
                    else:
                        raise InvalidMove("Could not Complete normal move - Try moving again")
                        pass
            except InvalidMove:
                pass


             # TODO: Check if instance of Move XY is King and update self.kings

    def king_destroyed_check(self, _takenPiece):
        if isinstance(_takenPiece, King):
            self.kings.remove(_takenPiece)

    def InitGame(self):
        # Initiate Game here
        print("Welcome To Basic Chess!")

        # random player order
        sides = ["w", "b"]
        random.shuffle(sides)

        self.reset_board()

        # represents a round
        forfeit = False
        while not forfeit or self.checkWin() is None:
            for side in sides:
                resignationPrompt = input("Press Enter to start turn, Anything else will exit>: ")
                if resignationPrompt != "":
                    forfeit = True
                else:
                    print(f"{side.upper()}'s Turn\n")
                    self.print_board()
                    self.make_move(side)
        print(f"Game Ended with {self.checkWin()}")
        exit()

    # Print Optimizations

    def printHorizontalCordNums(self):
        # Print Numbers for top of board
        # No Returns, just print statements
        count = 1
        for index in range(24):
            if (index == 1) | (index % 3 == 1):
                print(f"  {count}", end="")
                count += 1
        print()

    def print_board(self):
        # No Returns, just print statements

        self.printHorizontalCordNums()
        for keyParent, valueParent in self.board.items():  # Iterate over each item in dictionary
            print(f"{keyParent}", end="")
            for value in valueParent:  # Iterate over each value in the itemParent.Value
                print("|", end="")
                print(value, end="")
            print(f"|{keyParent}")
        self.printHorizontalCordNums()
        print("\n")
