class Plant:
    k = 1
    kind = 'green'
    
    def __init__(self):
        self.k = Plant.k
        Plant.k = self.k + 1
        if self.k > 3:
            Plant.name = lambda t: 'tree'
            Plant.k = 6
            
    def name(self):
        return kind
    
    def __repr__(self):
        s = self.name() + ' '
        return s + str(self.k)
    
class Flower(Plant):
    kind = 'pretty'
    
    def __repr__(self):
        s = self.smell() + ' '
        return s + Plant.__repr__(self)
    
    def smell(self):
        return 'bad'
    
class Rose(Flower):
    def name(self):
        return 'rose'
    
    def smell(self):
        return 'nice'