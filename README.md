n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

row_sums = [sum(row) for row in grid]

column_sums = [sum(row[col] for row in grid) for col in range(n)]

print("Row sums:")
for s in row_sums:
    print(s)

print("Column sums:")
for s in column_sums:
    print(s)
