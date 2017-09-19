# mutually recursive is even and odd function
def is_even_mutual(n):
    if n == 0:
        return True
    return is_odd_mutual(n - 1)

def is_odd_mutual(n):
    if n == 0:
        return False
    return is_even_mutual(n - 1)

# turn into one recurisve function
def is_even(n):
    if n == 0:
        return True
    if n-1 == 0:
        return False
    return is_even((n - 1) - 1)

def cascade(n):
    if n < 10:
        print n
    else:
        print n
        cascade(n // 10)
        print n
