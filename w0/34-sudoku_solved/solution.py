def sudoku_solved(sudoku):
    solved_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square = []
    squares = [square]*9
    for line in sudoku:
        if solved_list != sorted(line):
            return False
            
    square_index = 0;
    for x in range(0,3):
        for y in range(0, 3):
            squares[square_index+y].append(sudoku[y][x])
        square_index = square_index + 1

    for subsqare in squares:
        if sorted(subsqare) != solved_list:
            return False

    vertical = []
    for i in range(0,9):
        for line in sudoku:
            vertical.append(line[i])

        if sorted(vertical) != solved_list:
            
            return False
        vertical = []
    

    return True
