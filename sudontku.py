import tkinter as tk
from tkinter import messagebox

# Initialize the Sudoku grid
grid = [[0] * 9 for _ in range(9)]

def solve_sudoku():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(i, j, num):
                        grid[i][j] = num
                        if solve_sudoku():
                            return True
                        grid[i][j] = 0
                return False
    return True

def is_valid(row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def update_grid():
    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            if entry.get():
                grid[i][j] = int(entry.get())
            else:
                grid[i][j] = 0

    solve_sudoku()

    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(grid[i][j]))

def create_grid(root):
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tk.Entry(root, width=3, font=('Arial', 16), bg="#FFCCCC", fg="#000000")
            entry.grid(row=i, column=j, padx=3, pady=3)

            # Add extra spacing between every third row and column
            if i % 3 == 2:
                entry.grid(pady=(0, 9))
            if j % 3 == 2:
                entry.grid(padx=(0, 9))

            entry.insert(tk.END, "")

            row_entries.append(entry)
        entries.append(row_entries)

    return entries

def clear_grid():
    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.insert(tk.END, "")

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")
root.config(bg="#FFD9B3")  # Set background color of the main window

# Create the Sudoku grid
entries = create_grid(root)

# Create Solve and Clear buttons
solve_button = tk.Button(root, text="Solve", command=update_grid, bg="#FF5733", fg="#FFFFFF")
solve_button.grid(row=9, column=0, columnspan=4, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_grid, bg="#C70039", fg="#FFFFFF")
clear_button.grid(row=9, column=5, columnspan=4, pady=10)

# Run the main event loop
root.mainloop()
