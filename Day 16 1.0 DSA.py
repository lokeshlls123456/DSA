# Read dimensions
classes, days = map(int, input().split())

# Read first matrix (Week 1)
matrix1 = []
for _ in range(classes):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Read second matrix (Week 2)
matrix2 = []
for _ in range(classes):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Compute the element-wise sum of the two matrices
result_matrix = []
for i in range(classes):
    result_row = [matrix1[i][j] + matrix2[i][j] for j in range(days)]
    result_matrix.append(result_row)

# Print the resulting matrix
for row in result_matrix:
    print(" ".join(map(str, row)))