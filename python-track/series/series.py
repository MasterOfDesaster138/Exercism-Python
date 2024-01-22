def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif not series:
        raise ValueError("series cannot be empty")
    elif length > series:
        raise ValueError("slice length cannot be greater than series length")

    slices = []
    
    for index, num in series:
        end_pos = index + length
        slices.append(series[index:end_pos])
        
    return slices
