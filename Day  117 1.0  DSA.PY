# Read input
n = int(input())
product_ids = list(map(int, input().split()))

# Filter positive product IDs only
positive_ids = [pid for pid in product_ids if pid > 0]

# If no positive IDs, return -1
if not positive_ids:
    print(-1)
else:
    # Calculate middle index
    mid_index = (len(positive_ids) - 1) // 2
    # Print the product ID at the mid index
    print(positive_ids[mid_index])