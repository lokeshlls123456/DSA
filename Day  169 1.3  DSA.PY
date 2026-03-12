N = int(input().strip())

if N == 1:
    print(1)
elif N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    product = 1
    while N > 4:   
        product *= 3
        N -= 3
    product *= N   
    print(product)