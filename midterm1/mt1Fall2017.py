aaron, burr = 2, 5
aaron, burr = 4, aaron + 1

hamil = 10

def alex(hamil):
    def g(w):
        hamil = 2 * w
        print('blah: ' + str(hamil))
        print(hamil, w)
        w = hamil
        return hamil
    w = 5
    alex = g(w + 1)
    print(w, alex, hamil)
    
alex(3)
# print(aaron, burr)