n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = []
zero_count = 0
for num in arr:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
result.extend([0] * zero_count)
print(*result)