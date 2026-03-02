N = int(input().strip())
A = list(map(int, input().strip().split()))
if N <= 1:
    print(0)
else:
    unique_elements = sorted(set(A), reverse=True)
    
    if len(unique_elements) < 2:
        print(0)
    else:
        second_largest = unique_elements[1]
        count_second_largest = A.count(second_largest)
        print(count_second_largest)