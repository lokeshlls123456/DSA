N = int(input().strip())
A = list(map(int, input().strip().split()))
if N < 2:
    print(0)
else:
    A.sort(reverse=True)
    max_sum = A[0] + A[1]
    print(max_sum)