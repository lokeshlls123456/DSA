import math

N = int(input().strip())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(N):
    print("Premium Product")
else:
    print("Regular Product")