"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    # create a dict of all distinct items
    distinct_items = set(items)
    inventory = dict.fromkeys(distinct_items)

    # count each item and set the sum as dict value for the item
    for item in distinct_items:
        sum = items.count(item)   
        inventory[item] = sum
        
    return inventory


def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    # iterate through the items one by one
    for _ in range(len(items)):
        item = items.pop()
        # check if item already exists
        if item in inventory.keys():
            inventory[item] += 1
        # else add new item
        else:
            inventory.update([(item, 1)])
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for _ in range(len(items)):
        item = items.pop()
        if inventory[item] > 0:
            inventory[item] -= 1  
    return inventory


def remove_item(inventory: dict, item: list) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    # remove item if it exists in the dict
    if item in inventory.keys():
        inventory.pop(item)
        
    return inventory


def list_inventory(inventory: dict) -> list:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    # create a list of all key value pairs without value == 0 
    return [(key, value) for key, value in inventory.items() if value != 0]

   
