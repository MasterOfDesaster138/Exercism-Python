"""Instructions
        Your task is to determine the date and time one gigasecond after a certain date.

        A gigasecond is one thousand million seconds. 
        That is a one with nine zeros after it.

        If you were born on January 24th, 2015 at 22:00 (10:00:00pm), 
        then you would be a gigasecond old on October 2nd, 2046 at 23:46:40 (11:46:40pm).


Reading and Writing Long Numbers
    Code is more often read than it is written, and reading a big/long number within other text can be a challenge. 

    Here are two approaches to making numbers more readable:
        - Using underscores in Numeric Literals. 
            1_000_000 is more readable than 1000000, and 10_100_201_330 is easier to scan than 10100201330. 
            --> For more information, see PEP-0515.
        - Using exponential notation or scientific notation. 
            The e (or E) character followed by an integer represents the power of 10 
            by which the number preceding the e should be multiplied 
            (ie: 1e6, 1 is multiplied by 10 raised to the power of 6, which equals 1000000). 
            --> For more details, check out this reference on scientific notation.


Dates and Times in Python
    This exercise explores objects from Python's datetime module:
        - Official Python documentation on the datetime module
        - datetime objects
        - timedelta objects
"""
from datetime import timedelta, datetime


def add(moment: datetime) -> datetime:
    """Determines the date and time one gigasecond after a certain date."""
    gigasecond = 1e9
    interval = timedelta(seconds=gigasecond)
    
    return moment + interval
    
    
    
