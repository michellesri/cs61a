def find_pair_recursive(p):
    def find(n):
        if n >= 10:
            if p((n//10) % 10, n % 10):
                return True
            else:
                return find(n // 10)
        return False
    return find

def find_pair_iter(p):
    def find(n):
        while n >= 10:
            if p((n // 10) % 10, n % 10):
                return True
            else:
                n = n // 10
        return False
    return find
