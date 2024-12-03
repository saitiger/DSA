def rotate_matrix(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Create a new matrix with transposed dimensions
    rotated_matrix = [[0] * rows for _ in range(cols)]

    # Step 2: Transpose and reverse the rows
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix
