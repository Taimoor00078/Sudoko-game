# Sudoku Solver using Constraint Satisfaction Problem (CSP)

This project is a Python-based Sudoku solver that models the game as a Constraint Satisfaction Problem (CSP). It utilizes the **AC-3 algorithm** (Arc Consistency) for constraint propagation and **Backtracking Search** to efficiently find solutions to Sudoku puzzles.

## Project Structure

- `sudoku.py`: The main Python script containing the logic for the Sudoku solver (AC-3, Backtracking).
- `easy.txt`: A sample Sudoku puzzle of easy difficulty.
- `medium.txt`: A sample Sudoku puzzle of medium difficulty.
- `hard.txt`: A sample Sudoku puzzle of hard difficulty.
- `veryhard.txt`: A sample Sudoku puzzle of very hard difficulty.

## Features

- **AC-3 Algorithm**: Reduces the domain of each cell by enforcing arc consistency before and during the backtracking search.
- **Backtracking Search**: Explores possible valid values for empty cells.
- **Performance Metrics**: Tracks and outputs the number of **Backtrack Calls** and **Backtrack Failures** to evaluate the efficiency of the solver on different puzzle difficulties.

## How to Run

1. Ensure you have Python installed on your system.
2. The puzzle to solve is currently configured inside the `sudoku.py` file. By default, it is set to read `easy.txt` at the bottom of the script:
   ```python
   board = read_board("easy.txt")
   ```
   *To test other difficulty levels, you can edit this line in `sudoku.py` to point to `medium.txt`, `hard.txt`, or `veryhard.txt`.*
3. Open your terminal or command prompt, navigate to the project directory, and run the following command:
   ```cmd
   python sudoku.py
   ```

## Output 

The script will output the solved 9x9 Sudoku grid along with the performance metrics.

**Example Output:**
```text
Solved Sudoku:

7 8 4 9 3 2 1 5 6
6 1 9 4 8 5 3 2 7
2 3 5 1 7 6 4 8 9
5 7 8 2 6 1 9 3 4
3 4 1 8 9 7 5 6 2
9 2 6 5 4 3 8 7 1
4 5 3 7 2 9 6 1 8
8 6 2 3 1 4 7 9 5
1 9 7 6 5 8 2 4 3

Backtrack Calls: 50
Backtrack Failures: 0
```
