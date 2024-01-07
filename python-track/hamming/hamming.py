def distance(strand_a: str, strand_b: str) -> int:
    # The Hamming distance is only defined for sequences of equal length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        hamming = 0
        for i, cell_a in enumerate(strand_a):
            cell_b = strand_b[i]
            if cell_a != cell_b:
                hamming += 1
                    
        return hamming

