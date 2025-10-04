n = int(input().strip())
temperatures = list(map(int, input().strip().split()))
restored = temperatures[::-1]
print(*restored)