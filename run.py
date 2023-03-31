from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size, the number of ships,
    the players name and the board type (player or computer)
    Has methods for adding ships and guesses and printing the board
    """


    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    
    def print(self):
        for row in self.board:
            print(" ".join(row))


    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"


    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannor add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    My own invention ABOUT 10 LINES OF CODE
    """


def populate_board(board):
    """
    My own invention ABOUT 10 LINES OF CODE
    """


def make_guess(board):
    """
    My own invention ABOUT 40 LINES OF CODE
    """


def play_game(computer_board, player_board):
    """
    My own invention ABOUT 40 LINES OF CODE
    """


def new_game():
    """
    Starts a new game. Sets the board size and number of ships, restes the 
    scores and initialises the boards.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to Ultimate Battleships!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

new_game()
