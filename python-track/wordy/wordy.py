import re


def answer(question: str) -> int:
    """Calculates the result of a mathematical question provided in plain text.

    Parameters:
    question (str): The mathematical question in plain text.

    Returns:
    int: The calculated result of the question.

    Raises:
    ValueError: If the question contains invalid operators or syntax errors.

    The 'answer' function analyzes the given mathematical question provided in plain text format.
    It supports the four basic arithmetic operations (addition, subtraction, multiplication, and division) and expects
    clear formulations such as 'What is 5 plus 3?'.

    Examples:
    answer("What is 5 plus 3?") returns 8.
    answer("What is 6 divided by 2?") returns 3.

    If the question contains invalid operators or syntax, it raises a ValueError exception.
    """
    err1 = "unknown operation" 
    err2 = "syntax error" 
    result: int = 0
    number_pattern = r'^[-+]?\d*\.?\d+$'


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
        raise ValueError(err2)  # No numbers found in the question 

    # Search for all valid operators
    operators = re.findall(r'(plus|minus|multiplied by|divided by)', question)
   
    
    # Remove unnecessary words and punctuation
    question = question.removesuffix('?').removeprefix('What is ').replace('by', '')
    # Split the question into words into a list
    text = question.split()
    # check if the string is empty
    if not text:
        raise ValueError(err2)
    # check if there is only one number 
    elif len(numbers) == 1 and len(text) == 1:
        return int(numbers[0])
    # check whether we have a suitable number of operators and operands
    if len(operators) != len(numbers) - 1:
        raise ValueError(err2)

    operand = None
    
    for i, word in enumerate(text):
        print(f"Index{i}: {word}]") # for debugging
        
        # initialize previous and next word for comparsions
        if i > 0:
            previous_word = text[i - 1]
        if i < len(text) - 1:
            next_word = text[i + 1]
        
        # 2 numbers in a row are not allowed -> syntax error
        if re.match(number_pattern, word) and re.match(number_pattern, next_word):
            raise ValueError(err2)
        # check if the word matches any valid operator -> invalid operator
        elif word.isalpha() and word not in operator_functions:
            raise ValueError(err1)
        # 2 operators in a row are not allowed -> syntax error
        elif word in operator_functions and next_word in operator_functions:
            raise ValueError(err2)
        
        # check if we have a valid expression for calculation
        if word in operator_functions and i >= 1:
            if re.match(number_pattern, previous_word) and re.match(number_pattern, next_word):
                if operand is None:
                    operand = int(numbers.pop(0))
                else:
                    operand = result
                    
                result = operator_functions[word](operand, int(numbers.pop(0))) 
                next_word = ''
                
            
                
    # The calculated result of the question as an integer
    return result


if __name__ == '__main__':
    test_question = input("Enter a test question: ")
    print(answer(test_question))