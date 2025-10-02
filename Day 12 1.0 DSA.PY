N = int(input().strip())
A = list(map(int, input().strip().split()))
def find_missing_number(N, A):
    total_sum = N * (N + 1) // 2  
    current_sum = sum(A)          
    missing_number = total_sum - current_sum
    return missing_number
print(find_missing_number(N, A))