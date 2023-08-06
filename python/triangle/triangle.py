"""
Determine if a triangle is equilateral, isosceles, or scalene.

For a shape to be a triangle at all, all sides have to be of length > 0, 
and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.

In equations:

Let `a`, `b`, and `c` be sides of the triangle.
Then all three of the following expressions must be true:

```text
a + b ≥ c
b + c ≥ a
a + c ≥ b
```
"""

def is_it_a_triangle(a, b, c):
    """
        check if all sides are not null
    """
    if all([a, b, c]) and all([(a + b) >= c, (b + c) >= a, (a + c) >= b]):
        return True
    else:
        return False
    




def equilateral(sides):
    """
        An _equilateral_ triangle has all three sides the same length.
    """
    a, b, c = sides 

    if is_it_a_triangle(a, b, c):
        if a == b and b == c and c == a:
            return True
        else:
            return False
    else:
        return False



def isosceles(sides):
    """
        An _isosceles_ triangle has at least two sides the same length.
        (It is sometimes specified as having exactly two sides the same length, 
        but for the purposes of this exercise we'll say at least two.)
    """
    a, b, c = sides

    if is_it_a_triangle(a, b, c):
        if a == b or b == c or a == c:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    """
        A _scalene_ triangle has all sides of different lengths.
    """
    a, b, c = sides

    if is_it_a_triangle(a, b, c):
        if a != b and b != c and a != c:
            return True
        else:
            return False
    else:
        return False