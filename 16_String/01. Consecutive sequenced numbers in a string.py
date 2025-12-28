def is_consecutive_sequence(s: str) -> bool:
    """
    Check if the string is formed by consecutive increasing integers.
    
    Time: O(n²) in worst case (due to string concatenation)
    Space: O(n)
    """
    n = len(s)
    if n == 0:
        return False
    
    # Try starting lengths from 1 to n//2 + 1
    for start_len in range(1, n // 2 + 2):
        start = s[:start_len]
        
        # Skip if leading zero (except for single 0)
        if len(start) > 1 and start[0] == '0':
            continue
        
        num = int(start)
        generated = ""
        
        while len(generated) < n:
            generated += str(num)
            num += 1
            
            # Early stop if already too long
            if len(generated) > n:
                break
        
        if generated == s:
            return True
    
    return False


# Test cases
test_cases = [
    ("1234", True),       # 1,2,3,4
    ("91012", False),
    ("99100", True),      # 99,100
    ("010203", False),    # leading zeros invalid
    ("910911", True),     # 910,911
    ("1", True),
    ("", False),
    ("123456789101112", True),  # 1 to 12
]

for s, expected in test_cases:
    result = is_consecutive_sequence(s)
    print(f"String: {s:15} → {result} (Expected: {expected})")