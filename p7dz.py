import random


def exponentiation(num):
    i = 0
    while True:
        result = num ** i
        yield result
        if result > 100**20:
            break
        i += 1


iterator = iter(exponentiation(random.randint(2, 10)))
for elem in iterator:
    print(elem)
    print('------')