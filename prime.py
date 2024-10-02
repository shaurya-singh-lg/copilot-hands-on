def prime(n):
    """
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.




    Steps:
    1. If the number is less than 2, it is not prime.
    2. If the number is exactly 2, it is prime.
    3. If the number is even and greater than 2, it is not prime.
    4. For odd numbers greater than 2, check divisibility from 3 up to the square root of the number.
        - If any number in this range divides the number evenly, it is not prime.
        - If no numbers in this range divide the number evenly, it is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# create a function to do 5 unit tests of the code above
def test_prime():
    assert prime(1) == False
    assert prime(2) == True
    assert prime(3) == True
    assert prime(4) == False
    assert prime(5) == True
    print("All tests pass")

