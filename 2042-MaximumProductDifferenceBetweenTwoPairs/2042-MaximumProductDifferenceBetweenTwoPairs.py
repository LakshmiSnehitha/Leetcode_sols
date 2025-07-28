# Last updated: 7/28/2025, 3:29:11 PM
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        v=nums[0]*nums[1]
        n=len(nums)
        p=nums[n-1]*nums[n-2]
        return abs(v-p)
    
