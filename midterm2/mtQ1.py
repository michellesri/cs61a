class Plant:
    k = 1
    kind = 'green'
    
    def __init__(self):
        self.k = Plant.k
        Plant.k = self.k + 1
        if self.k > 3:
            Plant.name = lambda t: 'tree'
            Plant.k = 6