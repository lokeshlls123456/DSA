m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
result = []
for i in range(m):
    if i % 2 == 0: 
        result.extend(matrix[i])
    else:         
        result.extend(matrix[i][::-1])
print(" ".join(map(str, result)))