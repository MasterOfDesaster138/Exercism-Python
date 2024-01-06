def spiral_matrix(size: int) -> list[list[int]]:
    # Prepare the matrix filled with zeros 
    matrix = init_matrix(size)
    
    # Current number to write into the matrix
    num = 1

    top = 0
    left = 0
    right = size - 1 
    bottom = size - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


def init_matrix(size: int) -> list[list]:
    matrix = [[0] * size for _ in range(size)]
    return matrix
