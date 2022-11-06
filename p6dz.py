import random

try:
    result = []

    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        result.append(a/b)


    data = [10, 2, 2, 5, 4, 18, 0, 15, 8, 4]
    for key in data:
        c = random.choice(data)
        res = divider(key, c)
        result.append(res)


except ValueError:
    print(f'You`ve got ValueError, first int {key} is less then second {c}')
    print(result)
except IndexError as error:
    print('You`ve got IndexError: ', error)
    print(result)
except TypeError as error:
    print('You`ve got TypeError: ', error)
    print(result)
except ZeroDivisionError as error:
    print('You`ve got ZeroDivisionError: ', error)