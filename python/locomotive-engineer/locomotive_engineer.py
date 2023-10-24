"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """ 
    return list(args)


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.
    Implement a function fix_list_of_wagons() that takes two lists containing wagon IDs. 
    It should reposition the first two items of the first list to the end, 
    and insert the values from the second list behind (on the right hand side of) the locomotive ID (1). 
    The function should then return a list with the modifications.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    one, two, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, one, two]


def add_missing_stops(route: dict, **stops) -> dict:
    """Add missing stops to route dict.
    Your function should then return 
    the routing dict updated with an additional key 
    that holds a list of all the added stops in order.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # get a list of all stops 
    stop_list = list(stops.values())
    # add the list to the route dict
    route["stops"] = stop_list
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    pass


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    pass
