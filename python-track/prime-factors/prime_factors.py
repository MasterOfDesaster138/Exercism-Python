def factors(value):
    prime_factors = []
    divisor = 2
    
    while value > 1:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        
        divisor += 1
    
        if divisor**2 > value and value > 1: 
            prime_factors.append(value)
            break
        
    return sorted(prime_factors)
