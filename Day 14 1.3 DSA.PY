n = int(input().strip())
arr = list(map(int, input().strip().split()))
d = int(input().strip())
d = d % n
rotated = arr[d:] + arr[:d]
print(*rotated)