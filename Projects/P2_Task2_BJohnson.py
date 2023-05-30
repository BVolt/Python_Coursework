"""
Author: Brenden Johnson
Assignment: Project 3 - Task 2
Date: 3-2-2023
Course: 2520.01
"""
import time


# Task 2
def isPrime(n):
    for i in range(2,n):
        if (n % i) == 0:
          return False
    return True


def primeGenerator():
    n = 2
    primeCount = 0
    while True:
        if isPrime(n):
            if primeCount < 50 or primeCount >= 100:
                yield (n)
            primeCount += 1
        n += 1


def main():
    prime = primeGenerator()
    for i in range(50):
        print("Prime", i + 1, "=", next(prime))
    start = time.time()
    for i in range(1, 1001):
        if i == 1 or i == 1000:
            print("Prime", i+100, "=", next(prime))
        else:
            next(prime)
    print("Run time for generating last 1000 primes is approximately %.4f seconds" % float(time.time()-start))


if __name__ == "__main__":
    main()


"""
Output

Prime 1 = 2
Prime 2 = 3
Prime 3 = 5
Prime 4 = 7
Prime 5 = 11
Prime 6 = 13
Prime 7 = 17
Prime 8 = 19
Prime 9 = 23
Prime 10 = 29
Prime 11 = 31
Prime 12 = 37
Prime 13 = 41
Prime 14 = 43
Prime 15 = 47
Prime 16 = 53
Prime 17 = 59
Prime 18 = 61
Prime 19 = 67
Prime 20 = 71
Prime 21 = 73
Prime 22 = 79
Prime 23 = 83
Prime 24 = 89
Prime 25 = 97
Prime 26 = 101
Prime 27 = 103
Prime 28 = 107
Prime 29 = 109
Prime 30 = 113
Prime 31 = 127
Prime 32 = 131
Prime 33 = 137
Prime 34 = 139
Prime 35 = 149
Prime 36 = 151
Prime 37 = 157
Prime 38 = 163
Prime 39 = 167
Prime 40 = 173
Prime 41 = 179
Prime 42 = 181
Prime 43 = 191
Prime 44 = 193
Prime 45 = 197
Prime 46 = 199
Prime 47 = 211
Prime 48 = 223
Prime 49 = 227
Prime 50 = 229
Prime 101 = 547
Prime 1100 = 8831
Run time for generating last 1000 primes is approximately 0.3462 seconds
"""