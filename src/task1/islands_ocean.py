def count_islands(matrix):
    # The cell is considered to be a separate island if it's surrounded by 0s only.
    # This function counts number of such islands in a given MxN matrix
    island_count = 0

    def visit_neighbours(row, col):
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 1:
            matrix[row][col] = '-'
            # visit each neighbour using recursion
            visit_neighbours(row + 1, col)
            visit_neighbours(row - 1, col)
            visit_neighbours(row, col + 1)
            visit_neighbours(row, col - 1)
        # escape clause
        return

    # for each row
    for i in range(len(matrix)):
        # for each col
        for j in range(len(matrix[0])):
            # if the current cell is an island (1), increase the island count and visit its adjacent cells
            # if all of them are 0s -> it's an island
            # else these are small islands which compute one big island ->
            # need to replace them with '-' so that not to count them as separate island
            if matrix[i][j] == 1:
                island_count += 1
                visit_neighbours(i, j)

    return island_count


if __name__ == '__main__':
    # Testing
    m1 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1]
    ]
    assert count_islands(m1) == 2

    m2 = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ]
    assert count_islands(m2) == 3

    m3 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1]
    ]
    assert count_islands(m3) == 2
