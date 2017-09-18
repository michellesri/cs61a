def sum_digits_recursive(n):
    """Return the sum of digits of positive integer n."""
    if n < 10:
        return n
    else:
        last_digit = n % 10
        all_but_last = n // 10
        return sum_digits(all_but_last) + last
