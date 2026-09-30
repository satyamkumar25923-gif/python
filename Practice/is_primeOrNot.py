def is_prime(num):
    if num < 2:
        return False

    num1 = num - 1

    while num1 != 1:
        if num % num1 == 0:
            return False
        num1 -= 1

    return True


print(is_prime(76))
