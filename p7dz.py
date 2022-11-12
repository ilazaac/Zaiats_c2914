import random


def multiplier(num):
    a = 0
    while True:
        result = num ** a
        yield result
        if result > 100**20:
            break
        a += 1


iterator = iter(multiplier(random.randint(2, 10)))
for elem in iterator:
    print(elem)
    print('------')