class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store number and its index
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if complement already exists
            if complement in num_map:
                return [num_map[complement], i]

            # Store the current number with its index
            num_map[num] = i

        # Problem guarantees one solution, but just in case
        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))   # Output: [0, 1]
    print(sol.twoSum([3,2,4], 6))       # Output: [1, 2]
    print(sol.twoSum([3,3], 6))         # Output: [0, 1]
