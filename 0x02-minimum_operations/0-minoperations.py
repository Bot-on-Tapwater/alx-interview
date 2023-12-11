#!/usr/bin/python3
""" define minOperations function """


def minOperations(n):
    """ calculates fewest number of operations needed to
    result in exactly n H characters in the file"""
    # Get the least prime factors of n, and add them together
    if (n > 1):
        primes = []

        while (n > 1):
            leastFactor = primeFactors(n)

            primes.append(leastFactor)

            n = int(n / leastFactor)

            # print(f"new n is {n}")

        return (sum(primes))
    else:
        return (0)


def primeFactors(n):
    """Get the least prime factor of an integer"""

    isPrime = False

    for i in range(1, (n + 1)):
        # print(f"Testing if {i} is a prime number")
        for j in range(1, i):
            isPrime = False
            if (i % j == 0 and j != 1 and j != i):
                # print(f"{i} is not a prime number")
                isPrime = True
                break
        if (i != 1 and isPrime is False and n % i == 0):
            return (i)
