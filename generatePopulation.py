import random
def generate(n):
    array = []
    for i in range(n):
        temp = []
        for j in range(5):
            temp += [[random.randint(0,5),random.randint(0,5)]]
        array += [temp]
    return array
