N = int(input().strip())
A = list(map(int, input().strip().split()))
def count_climbable_houses(N, A):
    count = 0
    for stairs in A:
        if stairs % 3 == 0:
            count += 1
    return count
print(count_climbable_houses(N, A))