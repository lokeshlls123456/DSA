N = int(input().strip())

speed = 0
for i in range(1, N + 1):
    if N % i == 0:   # i is a factor
        speed += i

print(speed)