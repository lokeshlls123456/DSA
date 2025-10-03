N = int(input().strip())
arr = list(map(int, input().strip().split()))


def are_consecutive(arr):
    arr.sort()  
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:  
            return 0
    return 1
print(are_consecutive(arr))