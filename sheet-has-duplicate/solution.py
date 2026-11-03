def has_duplicate(nums):
    """Return True if any value appears at least twice."""
    # This is correct but too slow: it compares every pair of values.
    s = set()
    for n in nums:
        if n in s:
            return True 
        s.add(n)
        
    return False
