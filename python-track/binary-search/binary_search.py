def find(search_list, value) -> int :
    left, right = 0 , len(search_list) - 1
    # Otherwise, repeat the process on the part of the list that has not been eliminated.
    while left <= right:
        # Find the middle element of a sorted list and compare it with the item we're looking for.
        mid = (left + right) // 2
        # If the middle element is our item, then we're done!
        if search_list[mid] == value:
            return mid
        # If the middle element is greater than our item, we can eliminate that element and all the elements after it.
        elif search_list[mid] > value:
            right = mid - 1
        # If the middle element is less than our item, we can eliminate that element and all the elements before it.
        elif search_list[mid] < value:
            left = mid + 1 
    # If every element of the list has been eliminated then the item is not in the list.
    raise ValueError("value not in array")
    
