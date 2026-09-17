# Tic-Tac-Toe Game 🎮

A console-based Tic-Tac-Toe game built with Python. This project demonstrates fundamental programming concepts such as conditionals, loops, and data structures.

## Features

* Two-player Tic-Tac-Toe game using X and O.
* Random selection of the starting player.
* Input validation to prevent invalid moves.
* Automatic detection of wins and draws.
* Scoreboard to track player wins and draws.
* Move history displayed after each round.
* Option to play multiple rounds.

## Technologies Used

* Python 3
* Python standard library (`random` module)

## Data Structures Used

This project demonstrates the use of several Python data structures:

| Data Structure | Usage                                      |
| -------------- | ------------------------------------------ |
| List           | Represents the game board and move history |
| Tuple          | Stores winning combinations                |
| Set            | Tracks played cells                        |
| Dictionary     | Maintains the scoreboard                   |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jeetjat204-cpu/tic-tac-toe.git
```

### 2. Navigate to the project folder

```bash
cd tic-tac-toe
```

### 3. Run the game

```bash
python tictactoe.py
```

## How to Play

1. The game randomly selects Player X or Player O to start.
2. Enter your move using the format `row,col`.
3. Rows and columns are numbered from 0 to 2.
4. Players take turns placing their marks.
5. The first player to complete a row, column, or diagonal wins.
6. If all nine cells are filled without a winner, the game ends in a draw.
7. Choose whether to play another round.

## Learning Objectives

This project was created to practice:

* Conditional statements (`if`, `elif`, `else`)
* Iteration using `for` and `while` loops
* Lists, tuples, sets, and dictionaries
* Functions and modular programming
* Input validation
* Basic game logic

## Author

**Jeet Jat**

GitHub: [jeetjat204-cpu](https://github.com/jeetjat204-cpu)
