"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart.keys():
            current_cart[item] += 1
        else:
            current_cart[item] = 1
            
    return current_cart 


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    user_cart = dict.fromkeys(notes, 1)
    return user_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for key, value in cart.items():
        isle_mapping[key].insert(0, value)
        
    user_order = dict(sorted(isle_mapping.items(), reverse = True))
    return user_order


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    
    Create the function update_store_inventory(<fulfillment_cart>, <store_inventory>) that takes a "fulfillment cart" and a store inventory. 
    The function should reduce the store inventory amounts by the number "ordered" in the "fulfillment cart" and then return the updated store inventory. 
    Where a store item count falls to 0, the count should be replaced by the message 'Out of Stock'.
    """

    for key, value in fulfillment_cart.items():
        qty = value[0]
        
        if store_inventory[key][0] - qty <= 0:
            store_inventory[key][0] = "Out of Stock"
        else:
            store_inventory[key][0] -= qty

    return store_inventory