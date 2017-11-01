def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'insufficient funds'
        balance -= amount
        return balance
    return withdraw

john = make_withdraw(100)
john(25)
john(25)

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'insufficient funds'
        b[0] -= amount
        return b[0]
    return withdraw

steven = make_withdraw_list(100)
steven(25)

# NOTE: john and steven represent bank accounts opened

#interesting example of how nonlocal works.
    #run with pythontutor if confused
def f(x):
    x = 3
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)

total = b(3) + b(4)
