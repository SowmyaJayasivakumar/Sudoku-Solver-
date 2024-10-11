N = 9


# printing the soduko
def printing(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=" ")
        print()

# checks if same num in row , col, grid
def is_safe(grid, row, col, num):

    # for row checking
    for x in range(9):
        if grid[row][x] == num:
            return False

    # for col checking
    for x in range(9):
        if grid[x][col] == num:
            return False

    # for grid checking
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol] == num:
                return False
    return True

# solving soduko puzzle

def solve_sudoku(grid, row, col):

    # checks if we reached last col last row
    if (row == N-1 and col == N):
        return True

    # checks is last col is reached for each row and moves to next row

    if (col == N):
        row += 1
        col = 0

    # checks if the cell has num or empty (0):
    if grid[row][col] > 0:
        return solve_sudoku(grid,row,col+1)
    for num in range(1,N+1,1):
        if is_safe(grid,row,col,num):
            grid[row][col] = num

            if solve_sudoku(grid,row,col+1):
                return True

        grid[row][col] = 0
    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solve_sudoku(grid,0,0)):
    printing(grid)
else:
    print("No solution exists")







            
