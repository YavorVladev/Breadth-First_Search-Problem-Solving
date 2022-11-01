matrix = [[1, 0, 2, 2, 0],
          [0, 2, 0, 2, 0],
          [2, 2, 2, 2, 2],
          [0, 0, 2, 0, 2],
          [1, 2, 0, 0, 0]]

row, col = (2, 2)
p = 5


def FillProblem(matrix, row, col, p):
    start = matrix[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0:
        row, col = queue.pop()
        visited.add((row, col))
        matrix[row][col] = p
        for row, col in GetNeighbours(matrix, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return matrix


def GetNeighbours(matrix, row, col, start):
    indices = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in indices if IsValid(matrix, row, col) and matrix[row][col] == start]


def IsValid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


FillProblem(matrix, row, col, p)
[print(row) for row in matrix]
