""" Implement the following list operations:
    - `append` (_given two lists, add all items in the second list to the end of the first list_);
    - `concatenate` (_given a series of lists, combine all items in all lists into one flattened list_);
    - `filter` (_given a predicate and a list, return the list of all items for which `predicate(item)` is True_);
    - `length` (_given a list, return the total number of items within it_);
    - `map` (_given a function and a list, return the list of the results of applying `function(item)` on all items_);
    - `foldl` (_given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left_);
    - `foldr` (_given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right_);
    - `reverse` (_given a list, return a list with all the original items, but in reversed order_).
"""
from typing import Callable

def append(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, add all items in the second list to the end of the first list."""
    return list1 + list2


def concat(lists: list[list[int]]) -> list[int]:
    """Given a series of lists, combine all items in all lists into one flattened list."""
    flat_list = []
    
    for list in lists:
        for element in list:
            flat_list.append(element)
            
    return flat_list


def filter(function: Callable[[int], int], list: list[int]) -> list[int]:
    """Given a predicate and a list, return the list of all items for which `predicate(item)` is True."""
    valid_items = []
    
    for element in list:
        if function(element):
            valid_items.append(element)
            
    return valid_items


def length(list: list[int]) -> int:
    """Given a list, return the total number of items within it."""
    counter = 0 
    
    for item in list:
        counter += 1
        
    return counter


def map(function: Callable[[int], int], list: [int]) -> list[int]:
    """Given a function and a list, return the list of the results of applying `function(item)` on all items."""
    mapped_list = []
    
    for item in list:
        mapped_list.append(function(item))
        
    return mapped_list


def foldl(function: Callable[[int, int], int], list: list[int], initial: int) -> int:
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left."""
    accumulator = initial
    
    for item in list:
        accumulator = function(accumulator, item)
    
    return accumulator


def foldr(function: Callable[[int, int], int], list: list[int], initial: int) -> int:
    """Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right."""
    accumulator = initial
    reversed_list = reversed(list)
    
    for item in reversed_list:
        accumulator = function(accumulator, item)
    
    return accumulator


def reverse(list: list) -> list:
    """Given a list, return a list with all the original items, but in reversed order."""
    reversed_list = []
    
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    
    return reversed_list
