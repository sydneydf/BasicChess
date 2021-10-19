class Game:
    def __init__(self):
        self.board = {
            "A": [] * 8,
            "B": [] * 8,
            "C": [] * 8,
            "D": [] * 8,
            "E": [] * 8,
            "F": [] * 8,
            "G": [] * 8,
            "H": [] * 8,
        }

    def __str__(self):
        # return string representation of board here
        pass

    # Will this work??
    def resetBoard(self):
        backline = ["R", "H", "B", "Q", "K", "B", "H", "R"]

        for i in range(8):
            # Assign backline
            self.board["A"][i] = self.board["H"][i] = backline[i]
            # Assign Pawns
            self.board["B"][i] = self.board["G"][i] = "P"

    # Game Methods Here
