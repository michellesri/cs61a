# aaron, burr = 2, 5
# aaron, burr = 4, aaron + 1
# 
# hamil = 10
# 
# def alex(hamil):
#     def g(w):
#         hamil = 2 * w
#         print('blah: ' + str(hamil))
#         print(hamil, w)
#         w = hamil
#         return hamil
#     w = 5
#     alex = g(w + 1)
#     print(w, alex, hamil)
# 
# print(aaron, burr)
# alex(3)

def el(i, za):
    def angelica():
        return i + 1
    if i > 10:
        return za()
    elif i > 4:
        print(angelica())
        return el(i * i, za)
    else:
        return el(i * i, angelica)

el(3, el)

K = lambda x: lambda y: x
K(3) # Function
K(3)(2) # lambda
