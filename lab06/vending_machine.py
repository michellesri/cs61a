def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    snack_index = -1
    def inner():
        nonlocal snack_index
        if snack_index >= len(snacks) - 1:
            snack_index = -1
        snack_index += 1
        return snacks[snack_index]
    return inner
