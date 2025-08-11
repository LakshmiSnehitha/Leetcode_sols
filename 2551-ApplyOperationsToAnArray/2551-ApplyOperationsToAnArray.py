# Last updated: 8/11/2025, 11:13:47 PM
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Move zeros to the end
        result = [num for num in nums if num != 0]  # all non-zeros
        result.extend([0] * (n - len(result)))     # add zeros
        return result
