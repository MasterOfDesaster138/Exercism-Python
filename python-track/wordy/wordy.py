import re

def answer(question: str) -> int:
    err1 = "unknown operation"
    err2 = "syntax error"

    # Initialize variables to keep track of the current operator and numbers
    result = None
    operand_1 = None
    operand_2 = None
    current_operator = None

    # Define a dictionary to map operators to functions
    operator_functions = {
        'plus': lambda a, b: a + b,
        'minus': lambda a, b: a - b,
        'multiplied': lambda a, b: a * b,
        'divided': lambda a, b: a / b
    }

    # Search for numbers (including negative numbers)
    numbers = [int(match) for match in re.findall(r"(-?\d+)", question)]
    if not numbers:
        raise ValueError(err1)  # No numbers found in the question

    # Remove unnecessary words and punctuation
    question = question.replace('?', '').replace('What is', '')
    # Split the question into words
    text = question.split()
    # check if there is any text left
    if not text:
        raise ValueError(err2)

    for word in text:
        if word in operator_functions:
            if current_operator is not None:
                raise ValueError(err2)  # Two operators in a row is not allowed
            current_operator = word
        elif word.isnumeric():
            num = int(word)
            if operand_1 is None:
                operand_1 = num
            else:
                if current_operator is None:
                    raise ValueError(err2)  # Two numbers without an operator is not allowed
                operand_2 = num
                if result is not None:
                    operand_1 = result
                result = operator_functions[current_operator](operand_1, operand_2)
                operand_1 = None
                current_operator = None

    if current_operator is not None or operand_1 is not None:
        raise ValueError(err2)  # Check for errors with the operators and operands

    return result
