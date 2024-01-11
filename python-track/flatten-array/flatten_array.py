"""Instructions
Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For example:

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
"""


def flatten(iterable: list):
    result = []
    
    for item in iterable:
        if isinstance(item, (list, tuple)):
            # call recursively the function for nested lists or tuples
            result.extend(flatten(item))
        elif item is not None:  
            # Add non-none values to the result
            result.append(item)
                
    return result
