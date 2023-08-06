"""
An [Armstrong number][armstrong-number] is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

- 9 is an Armstrong number, because `9 = 9^1 = 9`
- 10 is *not* an Armstrong number, because `10 != 1^2 + 0^2 = 1`
- 153 is an Armstrong number, because: `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
- 154 is *not* an Armstrong number, because: `154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190`

Write some code to determine whether a number is an Armstrong number.
"""


def is_armstrong_number(number):
    """ 
    A function to determine whether a number is an Armstrong number.
    :param number: int - number to determine.
    :return: bool - is number an Armstrong number?
    """
# determine the exponent from number
    number_length = len(str(number))
    number_length = int(number_length)
     
# split number into single digits and store them into a list
    digit_list = list(str(number))
    digit_list = list(map(int, digit_list))

# multiply every digit with exponent and store the values into a list
    digits_with_exponent = []
    for i in digit_list:
        current_power_value = i ** number_length
        digits_with_exponent.append(current_power_value)
    
# sum up all powered digits
    power_sum = sum(digits_with_exponent)

# check if number is an Armstrong number and return
    if number == power_sum:
        return True
    else:
        return False
    


    
