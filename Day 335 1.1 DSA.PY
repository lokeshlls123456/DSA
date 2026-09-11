def clock_product(X, Y):
    product = X * Y
    result = product % 12
    if result == 0:
        result = 12
    return result

X = int(input())
Y = int(input())

print(clock_product(X, Y))