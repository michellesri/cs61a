x = 1
def f(n):
    def g():
        return n + x
    x = n + 5
    if n % 3 == 0:
        return g
    else:
        return f(n + 1)
    
x = 10
z = f(2)
q = x + z() # z returns g() where n = 3 and x = 8
print(q) # returns 21