def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    This function should return the value of the exchanged currency.
    """

    foreign_currency = budget / exchange_rate
    return foreign_currency


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    This function should return the amount of money that is left from the budget.
    """

    left_budget = budget - exchanging_value
    return left_budget


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.

    This exchanging booth only deals in cash of certain increments.
    The total you receive must be divisible by the value of one "bill" or unit,
    which can leave behind a fraction or remainder. Your function should return only
    the total value of the bills (excluding fractional amounts) the booth would give back.
    Unfortunately, the booth gets to keep the remainder/change as an added bonus.
    """

    value_of_bills = number_of_bills * denomination
    return value_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.

    This function should return the number of currency bills that you can receive within the given budget.
    In other words: How many whole bills of currency fit into the amount of currency you have in your budget?
    Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly.
    Effectively, you are rounding down to the nearest whole bill/denomination.
    """

    number_of_bills = budget // denomination
    return number_of_bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.

    This function should return the leftover amount that cannot be exchanged from your budget given
    the denomination of bills. It is very important to know exactly how much the booth gets to keep.
    """

    leftover_of_bills = budget % denomination
    return leftover_of_bills


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    Create the exchangeable_value() function, taking budget, exchange_rate, spread, and denomination.
    Parameter spread is the percentage taken as an exchange fee, written as an integer.
    It needs to be converted to decimal by dividing it by 100. If 1.00 EUR == 1.20 USD and the spread is 10,
    the actual exchange rate will be: 1.00 EUR == 1.32 USD because 10% of 1.20 is 0.12, and this additional fee
    is added to the exchange.
    This function should return the maximum value of the new currency after calculating the exchange rate
    plus the spread. Remember that the currency denomination is a whole number, and cannot be sub-divided.

    Note: Returned value should be int type.
    """

    spread_rate = spread / 100
    spread_value = exchange_rate * spread_rate
    total_exchange_rate = exchange_rate + spread_value
    full_exchange = budget / total_exchange_rate
    exchanged_value = full_exchange // denomination
    exchanged_bills = exchanged_value * denomination
    return exchanged_bills
