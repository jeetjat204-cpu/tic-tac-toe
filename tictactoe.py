"""
Tic-Tac-Toe Game
=================
A console-based Tic-Tac-Toe program built to demonstrate:
- Conditionals (if/elif/else)
- Iteration (for/while loops)
- Data structures: list, tuple, set, dictionary
- Arrays (using Python lists as arrays / grid)
"""

import random

# ---------------------------------------------------------
# DATA STRUCTURES SETUP
# ---------------------------------------------------------

# ARRAY (list of lists) -> represents the 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# TUPLE -> stores all winning combinations (immutable, since these never change)
WINNING_COMBOS = (
    ((0, 0), (0, 1), (0, 2)),  # row 1
    ((1, 0), (1, 1), (1, 2)),  # row 2
    ((2, 0), (2, 1), (2, 2)),  # row 3
    ((0, 0), (1, 0), (2, 0)),  # col 1
    ((0, 1), (1, 1), (2, 1)),  # col 2
    ((0, 2), (1, 2), (2, 2)),  # col 3
    ((0, 0), (1, 1), (2, 2)),  # diagonal
    ((0, 2), (1, 1), (2, 0)),  # anti-diagonal
)

# SET -> keeps track of which cells have already been played (fast lookup)
played_cells = set()

# DICTIONARY -> keeps score for each player
scoreboard = {"X": 0, "O": 0, "Draws": 0}

# LIST -> keeps a move history log, e.g. [("X", (0,0)), ("O", (1,1)), ...]
move_history = []


# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------

def print_board(board):
    """Prints the current board using iteration."""
    print()
    for i, row in enumerate(board):          # ITERATION (for loop)
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()


def get_move(player):
    """Asks the current player for a move and validates it using conditionals/loops."""
    while True:                              # ITERATION (while loop)
        move = input(f"Player {player}, enter your move as row,col (0-2 0-2): ")
        try:
            row, col = (int(x.strip()) for x in move.split(","))
        except ValueError:
            print("Invalid format. Please enter two numbers separated by a comma.")
            continue

        # CONDITIONALS to validate input
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of range. Rows and columns must be between 0 and 2.")
        elif (row, col) in played_cells:      # SET lookup
            print("That cell is already taken. Choose another.")
        else:
            return row, col


def make_move(board, player, row, col):
    """Places the player's mark on the board and updates data structures."""
    board[row][col] = player
    played_cells.add((row, col))              # add to SET
    move_history.append((player, (row, col)))  # add to LIST


def check_winner(board, player):
    """Checks all winning combinations (tuple of tuples) using iteration + conditionals."""
    for combo in WINNING_COMBOS:               # ITERATION over TUPLE
        marks = [board[r][c] for r, c in combo]  # LIST comprehension
        if all(mark == player for mark in marks):  # CONDITIONAL check
            return True
    return False


def board_full():
    """Checks if the board is full using the SET of played cells."""
    return len(played_cells) == 9


def reset_game():
    """Resets the board and related data structures for a new round."""
    global board, played_cells, move_history
    board = [[' ' for _ in range(3)] for _ in range(3)]
    played_cells = set()
    move_history = []


def choose_starting_player():
    """Randomly picks who starts — demonstrates use of a list and random.choice."""
    players = ["X", "O"]                       # LIST
    return random.choice(players)


def play_round():
    """Plays a single round of tic-tac-toe."""
    current_player = choose_starting_player()
    print(f"\nPlayer {current_player} goes first this round!")

    print_board(board)

    while True:                                 # ITERATION (game loop)
        row, col = get_move(current_player)
        make_move(board, current_player, row, col)
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins this round!")
            scoreboard[current_player] += 1     # update DICTIONARY
            break
        elif board_full():
            print("It's a draw!")
            scoreboard["Draws"] += 1            # update DICTIONARY
            break
        else:
            # switch player using a CONDITIONAL
            current_player = "O" if current_player == "X" else "X"

    print("\nMove history for this round:")
    for player, pos in move_history:            # ITERATION over LIST of TUPLES
        print(f"  {player} -> {pos}")


def print_scoreboard():
    """Prints the scoreboard dictionary."""
    print("\n--- Scoreboard ---")
    for player, wins in scoreboard.items():     # ITERATION over DICTIONARY
        print(f"{player}: {wins}")
    print("------------------\n")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:                                  # ITERATION (main loop)
        reset_game()
        play_round()
        print_scoreboard()

        again = input("Play another round? (y/n): ").strip().lower()
        if again != "y":                          # CONDITIONAL
            print("Thanks for playing! Final scores:")
            print_scoreboard()
            break


if __name__ == "__main__":
    main()