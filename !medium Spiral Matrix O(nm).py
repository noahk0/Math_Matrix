def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    i, j, spiral, l = 0, 0, [], len(matrix) * len(matrix[0])

    while 1:
        check = len(spiral)
            
        while j + 1 < len(matrix[0]) and matrix[i][j + 1] < 101:
            spiral.append(matrix[i][j])
            matrix[i][j] = 101
            j += 1

        while i + 1 < len(matrix) and matrix[i + 1][j] < 101:
            spiral.append(matrix[i][j])
            matrix[i][j] = 101
            i += 1

        while j and matrix[i][j - 1] < 101:
            spiral.append(matrix[i][j])
            matrix[i][j] = 101
            j -= 1

        while i and matrix[i - 1][j] < 101:
            spiral.append(matrix[i][j])
            matrix[i][j] = 101
            i -= 1

        if check == len(spiral):
            return spiral + [matrix[i][j]]
