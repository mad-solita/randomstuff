import math

PUSH_LIMIT = 12

def piston_sequence(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative")
    
    sequence = []
    remainder =  n % PUSH_LIMIT
    
    if remainder > 0:
        sequence.append((remainder, 1))
    
    end = remainder
    while end < n:
        end = min(end + PUSH_LIMIT, n)
        sequence.append((end, 1))
    
    return sequence

if __name__ == "__main__":
    n = int(input('Must be int: '))
    seq = piston_sequence(n)
    for start, end in seq:
        print(f"[{start} -> {end}]")