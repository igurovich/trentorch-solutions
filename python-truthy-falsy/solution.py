def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    # None is always falsy
    if value is None:
        return False

    # The two bool singletons
    if value is True:
        return True
    if value is False:
        return False

    cls = type(value)

    if cls in (int, float, complex):
        # Zero of any numeric type is falsy; NaN is truthy (NaN != 0)
        return value != 0

    if cls in (str, bytes, bytearray, list, tuple, dict, set, frozenset, range):
        # Empty containers are falsy
        return len(value) != 0


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for value in values:
        if bool(value):  # explicit truthiness check
            return value
    return None
