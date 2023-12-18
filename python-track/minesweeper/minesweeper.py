error_msg = "The board is invalid with current input."

def annotate(minefield: list) -> list:
    
    if not minefield:
        return []
    elif validate_boardsize(minefield):
        result = []
        rows = minefield
        
        # iterate trough each element of the minefield
        for y, row in enumerate(rows):
            row_counts = ""
            
            for x, element in enumerate(row):
                element_position = (x, y)
                
                # get the transformed value for the element
                if element == '*':
                    cell = '*'
                else:
                    cell = eval_mine_counts(rows, element_position)
                row_counts += cell
                
            result.append(row_counts)
        return result
    else:
        raise ValueError(error_msg)


def validate_boardsize(minefield: list) -> bool:
    """ Validates the size of a Minesweeper game board.

        Parameters:
        - minefield (list): 2D list representing the Minesweeper game board.
        
        Returns:
        - bool: True if all rows in the minefield have the same length, False otherwise.
    """
    # check if board contains only valid characters
    valid_characters = {'*', ' '}
    if not all(set(row) <= valid_characters for row in minefield):
        return False
    
    # get the length of the first row as reference
    row_size = len(minefield[0])
    
    # check if each row has the same length
    for row in minefield:
        if len(row) != row_size:
            return False
    return True


def eval_mine_counts(rows: list, field: tuple) -> str:
    """Evaluates the mine counts for a given element in a Minesweeper game board.

    Parameters:
    - rows (list): A list representing the rows of the Minesweeper game board.
    - columns (list): A list representing the columns of the Minesweeper game board.
    - field (tuple): A tuple representing the coordinates (x, y) of the element.

    Returns:
    - str: The count of adjacent mines as a string. If there are no adjacent mines, returns an empty string.
    """
    neighbors = get_neighbors(rows, field)
    mine_sum = neighbors.count("*")
    if mine_sum > 0:
        return str(mine_sum)
    else:
        return " "
    
    
def get_neighbors(matrix: list, field: tuple):
    """Retrieves the values of adjacent fields for a given element in a Minesweeper game board.

    Parameters:
    - matrix (list): A 2D list representing the Minesweeper game board.
    - field (tuple): A tuple representing the coordinates (x, y) of the element.

    Returns:
    - list: A list of values of adjacent fields.
    """
    x, y = field
    height = len(matrix)
    width = len(matrix[0])
    neighbors = []
    
    # iterate over the adjacent fields (horizontally, vertically and diagonally)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j
            
            # Check whether the coordinates are valid and are not the current element
            if 0 <= new_x < width and 0 <= new_y < height and (i != 0 or j != 0):
                neighbors.append(matrix[new_y][new_x])
    
    return neighbors