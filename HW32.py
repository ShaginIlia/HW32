def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        d = 2
        while number % d != 0:
            d += 1
        if d == number:
            print(f'Число {number} - простое')
        if d != number:
            print(f'Число {number} - составное')
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


summ = sum_three(19, 3, 3)
summ

