class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such an element was found
        if i >= 0:
            # Find the element just larger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the part after i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
nums = [1, 2, 3]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]

nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 2, 3]

nums = [1, 1, 5]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 5, 1]
