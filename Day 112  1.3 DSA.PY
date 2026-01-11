n1 = int(input().strip())
n2 = int(input().strip())

count = 0

for num in range(n1, n2 + 1):
    num_str = str(num)
    if len(num_str) == len(set(num_str)):
        count += 1

print(count)