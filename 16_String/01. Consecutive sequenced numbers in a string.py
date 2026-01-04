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
if __name__ == "__main__":
    s = "1234"
    print(is_consecutive_sequence(s))   # True

    s = "99100"
    print(is_consecutive_sequence(s))   # True

    s = "91012"
    print(is_consecutive_sequence(s))   # False

    s = "010203"
    print(is_consecutive_sequence(s))   # False

    s = "123456789101112"
    print(is_consecutive_sequence(s))   # True
