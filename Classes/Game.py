import random
import time
from string import ascii_lowercase
import CSV_Writer
from Classes.InvalidMove import InvalidMove

# Long class imports because in different sub directories
from Classes.Pieces.Bishop import Bishop
from Classes.Pieces.King import King
from Classes.Pieces.Knight import Knight
from Classes.Pieces.Pawn import Pawn
from Classes.Pieces.Queen import Queen
from Classes.Pieces.Rook import Rook
from Classes.Pieces.Piece import Piece


# TODO: CHECK main.py for TODO list

# Main Game/Board Interactivity Class
class Game:
    # These are hardcoded escaped colours that will custom color terminal text
    # Hardcoded here because they don't get modified
    move_response: str = '\033[96m'
    warning: str = '\033[93m'
    won: str = '\033[92m'
    failed: str = '\033[91m'
    bold: str = '\033[1m'
    endc: str = '\033[0m'

    # self.board indexing in functions may cause false positives in PyCharm IDE
    def __init__(self):
        # store king states in memory for quick ref without searching
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
        self.horizontalLen: int = 19
        self.writer: CSV_Writer = None
        self.InitGame()
        self.successfulMove: bool = False
        self.winner: King

    def reset_board(self):

        teams = ["w", "b"]

        # Init Pawns
        for i in range(0, 8):
            self.board["b"][i] = Pawn(f"b{i}", teams[0])
            self.board["g"][i] = Pawn(f"b{i}", teams[1])

        backLinePlace = {"R": [0, 7], "N": [1, 6], "B": [2, 5], "Q": [3], "K": [4]}

        # TODO: NEED TO CONSOLIDATE THIS CODE
        # Init Rooks
        for pos in backLinePlace["R"]:
            self.board["a"][pos] = Rook(f"a{pos}", "w")
            self.board["h"][pos] = Rook(f"h{pos}", "b")

        # Init Knights
        for pos in backLinePlace["N"]:
            self.board["a"][pos] = Knight(f"a{pos}", "w")
            self.board["h"][pos] = Knight(f"h{pos}", "b")

        # Init Bishops
        for pos in backLinePlace["B"]:
            self.board["a"][pos] = Bishop(f"a{pos}", "w")
            self.board["h"][pos] = Bishop(f"h{pos}", "b")

        # Init Queens
        self.board["a"][backLinePlace['Q'][0]] = Queen(f"a{backLinePlace['Q'][0]}", "w")
        self.board["h"][backLinePlace['Q'][0]] = Queen(f"h{backLinePlace['Q'][0]}", "b")

        # Init Kings
        self.board["a"][backLinePlace['K'][0]] = King(f"a{backLinePlace['K'][0]}", "w")
        self.board["h"][backLinePlace['K'][0]] = King(f"h{backLinePlace['K'][0]}", "b")

    # Check if game should be over
    def checkWin(self):
        kings = []
        for xRow, YList in self.board.items():
            # enumerate iterates over a list and returns current iteration loop + item
            for Ycord, item in enumerate(YList):
                if isinstance(item, King):
                    kings.append(item)
        if len(kings) == 1:
            self.winner = kings[0]
            print("\n" + self.won + self.winner.colour + " wins!" + self.endc)
            print(self.failed + "Game Over! ..." + self.endc)
            time.sleep(1)
            print(self.failed + "Exiting" + self.endc)
            exit()

    # Split move into workable cords for self.board
    def move_splitter(self, _move_split: str) -> tuple[str, int]:
        return _move_split[0], int(_move_split[1])

    # Take in starting move and end move and move type and check iteratively if there is any pieces blocking moves
    def check_emptySpace(self, _start_move, _end_move, _move_type):
        pass

    # this just gets proper input of a move choice
    def input_getSquare(self, msgPrompt: str) -> str:
        properMoveFormat = False
        xLetter = None
        yInt = None
        print(Game.warning + msgPrompt + Game.endc)
        while not properMoveFormat:
            potentialMove = input(Game.warning + "Please select a valid coordinate for this>: " + Game.endc)
            if len(potentialMove) == 2:

                xLetter, yString = potentialMove

                try:
                    yInt = int(yString)
                except ValueError or IndexError:
                    break

                if xLetter not in self.board.keys() or yInt not in range(0, 8):
                    break

                # If all not fail then while loop passes
                print(f"\nInput Move Validator: Valid Cord of {xLetter} {yInt}")
                print(f"Converting move to board friendly {xLetter} {yInt - 1}\n")
                properMoveFormat = True

            else:
                print(self.failed + "Please Choose a proper board location" + self.endc)

        return f"{xLetter.lower()}{yInt - 1}"

    # Initiate castle move
    def castle_init(self, _combinedSelectCord, _combinedMoveCord):
        currXstr, currYint = self.move_splitter(_combinedSelectCord)
        moveXstr, moveYint = self.move_splitter(_combinedMoveCord)

        # False Positives
        selectedPiece: King = self.board[currXstr][currYint]
        squareToTake: Rook = self.board[moveXstr][moveYint]

        if not selectedPiece.hasMoved == squareToTake.hasMoved:

            try:
                # 5 < 8
                if currYint < moveYint:
                    for Ycheck in range(currYint + 1, moveYint):
                        if self.board[moveXstr][Ycheck] != "  ":
                            raise InvalidMove("Cannot Castle if space between is not empty")
                # 5 > 1
                else:
                    for Ycheck in range(currYint - 1, moveYint, -1):
                        if self.board[moveXstr][Ycheck] != "  ":
                            raise InvalidMove("Cannot Castle if space between is not empty")

            except InvalidMove as msg:
                print(msg)
                return

            # To Move adjacent to king to protect
            rookY = 0
            if moveYint == 0:
                rookY = 1
            else:
                rookY = 6

            selectedPiece.currentLocation = f"{moveXstr}{moveYint}"
            squareToTake.currentLocation = f"{currXstr}{rookY}"

            self.board[moveXstr][moveYint], self.board[currXstr][rookY] = selectedPiece, squareToTake
            selectedPiece.hasMoved = squareToTake.hasMoved = True
            return True

    # Initiate custom pawn move, Can probably consolidate half of this into pawn class
    def pawn_move(self, _combinedSelectCord, _combinedMoveCord):
        print("DEBUGGING: Pawn Move triggered")
        currXstr, currYint = self.move_splitter(_combinedSelectCord)
        moveXstr, moveYint = self.move_splitter(_combinedMoveCord)

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
            for Ycheck in range(currYint - 1, currYint + 2, 2):
                squareCheck = self.board[moveXstr][Ycheck]
                if isinstance(squareCheck, Piece):
                    legal_moves.append((ascii_lowercase[currXint + foward], Ycheck))

        # for move_cord in legal_moves:
        #     print(f"DEBUGGING Legal move cords: {move_cord[0]}, {move_cord[1]}")

        if (moveXstr, moveYint) in legal_moves:
            selectedPiece.currentLocation = _combinedMoveCord
            selectedPiece.hasMoved = True
            # print(f"Attempting to move from {_combinedSelectCord} TO move square on {_combinedMoveCord}")
            self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, "  "
            return True

    # Else move, a normal move and not a special move like the above moves
    def normal_move(self, _combinedSelectCord, _combinedMoveCord):
        print("DEBUGGING: Normal Move triggered")
        currXstr, currYint = self.move_splitter(_combinedSelectCord)
        moveXstr, moveYint = self.move_splitter(_combinedMoveCord)

        selectedPiece = self.board[currXstr][currYint]
        squareToTake = self.board[moveXstr][moveYint]

        legal_moves = selectedPiece.potential_moves()
        for tupleCord in legal_moves:
            # print(f"DEBUGGING Legal move cords: {tupleCord[0]}, {tupleCord[1]}")
            if (moveXstr, moveYint) == (tupleCord[0], tupleCord[1]):
                selectedPiece.currentLocation = _combinedMoveCord
                self.board[moveXstr][moveYint], self.board[currXstr][currYint] = selectedPiece, "  "
                return True
        return

    # initiate move on board
    # check if not pawn and then initiate capture method

    # designed to return record logging of moves
    # TODO: ROOK, BISHOP QUEEN NEED TO CHECK IF THERE IS A PIECE IN BETWEEN BEFORE MOVE
    def make_move(self, _colour) -> list[str, str]:

        # Here we handle all move possibilities

        # MUST GET A VALID PIECE
        selectSquare: str = "  "  # Raw combined string only used via move_splitter(selectSquare)
        currXstr: str = " "  # X Letter to reference the dict
        currYint: int = 99  # y int to reference list index of given X dict

        # Pre Hoisting these variable for higher scope access for return
        moveXstr: str = " "
        moveYint: int = 99

        # Pre Hoisting these variables for user-friendly feedback statements because we can't re-reference board after
        # it gets updated

        # These will get updated to store a copy of the items at its given point in time and on board
        selectedPiece = "  "  # Represents specific select spot of dict list
        squareToTake = None

        while selectedPiece == "  ":
            # returns str, int cords
            selectSquare = self.input_getSquare("Please select one of your OWN piece")
            currXstr, currYint = self.move_splitter(selectSquare)
            proposedSelected = self.board[currXstr][currYint]
            if proposedSelected != "  " and proposedSelected.colour == _colour:
                selectedPiece = self.board[currXstr][currYint]
            else:
                print(Game.failed + f"Non Valid piece selected: {selectSquare}\n" + Game.endc)

        selectedPiece: Piece

        self.successfulMove = False
        debug_failedCycles = 0
        while not self.successfulMove:
            if debug_failedCycles > 0:
                print(f"Failed Debug cycles = {debug_failedCycles}")
            try:
                moveSquare = self.input_getSquare("Please enter a square to move to")
                moveXstr, moveYint = self.move_splitter(moveSquare)
                moveXstr: str  # X Letter to reference the dict
                moveYint: int  # y int to reference list index of given X dict

                squareToTake = self.board[moveXstr][moveYint]  # Error here might be false positive

                # Check for pawn moves
                if isinstance(selectedPiece, Pawn):
                    # print(f"DEBUGGING: Pawn Move triggered on converted: {moveSquare}")
                    if self.pawn_move(selectSquare, moveSquare):
                        self.successfulMove = True
                    else:
                        raise InvalidMove("Pawn move failed")
                elif squareToTake == "  ":
                    print(f"DEBUGGING: Empty Take Move triggered {moveSquare}")

                    if self.normal_move(selectSquare, moveSquare):
                        self.successfulMove = True
                    else:
                        raise InvalidMove(f"Empty Space move not in valid moveset: {moveSquare}")

                    # Check for KING/ROOK CASTLING FIRST
                    # Only King can INITIATE CASTLE
                elif isinstance(selectedPiece, King) and isinstance(squareToTake, Rook):
                    if selectedPiece.colour == squareToTake.colour:
                        print(
                            f"DEBUGGING: Castle Move triggered for {selectedPiece} at {selectedPiece.currentLocation}")
                        if self.castle_init(selectSquare, moveSquare):
                            self.successfulMove = True
                        else:
                            raise InvalidMove(f"Castling move failed on {moveSquare}")
                    else:
                        # Else must be opposite colour King attacking Rook, Very niche but may happen
                        if self.normal_move(selectSquare, moveSquare):
                            self.successfulMove = True
                        else:
                            raise InvalidMove("King cannot take opposite teams Rook?")

                # Eliminate Team-Kill AFTER castling check
                elif selectedPiece.colour == squareToTake.colour:
                    print("DEBUGGING: Team-Kill Check")
                    raise InvalidMove("Cannot take own piece - choose again")

                else:
                    print("Else of Move")
                    if self.normal_move(selectSquare, moveSquare):
                        self.successfulMove = True
                    else:
                        raise InvalidMove("Could not Complete normal move - Try moving again")

            except InvalidMove as msg:
                print(msg)
                debug_failedCycles += 1
                self.print_board()
                continue

        # Grab Type __name__ of piece for selectedSquare print and its coordinate
        # Grab Type __name__ of piece for move print and its coordinate
        # Present as a print for user

        item_toMoveOnStatement = (
            "*empty square*" if squareToTake == "  " else f"{squareToTake.colour}'s {type(squareToTake).__name__}")
        print(
            Game.move_response + f"\n{selectedPiece.colour}'s {type(selectedPiece).__name__} - {currXstr}{currYint + 1} has taken {item_toMoveOnStatement} at {moveXstr}{moveYint + 1}\n" + Game.endc)

        # Only want this return if move successful
        # +1ing the ints for user-friendly processing
        # print(f"DEBUGGING: Testing make_move return {currXstr}{currYint + 1} {moveXstr}{moveYint + 1}")
        return [f"{currXstr}{currYint + 1}", f"{moveXstr}{moveYint + 1}"]

    def InitGame(self):
        # Initialize custom CSV_Writer Object
        self.writer = CSV_Writer.CSV_Writer()

        # Initiate Game here
        print("Welcome To Basic Chess!")

        # random player order
        sides = ["w", "b"]
        random.shuffle(sides)

        self.reset_board()

        # represents a round
        end = False
        while not end:
            move_row2Write = {'wFrom': '', 'wTo': '', 'bFrom': '', 'bTo': ''}
            for side in sides:
                resignationPrompt = input(f"Press {Game.warning}Enter key{Game.endc} to start turn, Anything else "
                                          f"will exit>: ")
                if resignationPrompt != "":
                    end = True
                else:
                    print("\n" + Game.bold + f"{side.upper()}'s Turn\n" + Game.endc)
                    self.print_board()
                    recorded_move = self.make_move(side)  # TODO: Get return info from here and add to writer list
                    if side == "w":
                        move_row2Write['wFrom'], move_row2Write['wTo'] = recorded_move
                    else:
                        move_row2Write['bFrom'], move_row2Write['bTo'] = recorded_move

                    if self.checkWin():
                        end = False
            # Write out the dict to csv after full move completion
            self.writer.row_write(move_row2Write)
        print("Game Forfeited")
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
        for dictXkey, listY in self.board.items():  # Iterate over each item in dictionary
            print(f"{dictXkey}", end="")
            for Yvalue in listY:  # Iterate over each value in the itemParent.Value
                print("|", end="")
                print(Yvalue, end="")
            print(f"|{dictXkey}")
        self.printHorizontalCordNums()
        print("\n")
