# Last updated: 7/28/2025, 3:30:18 PM
# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         nums.sort()
#         res=0
#         s=len(nums)
#         for i in range(1,len(nums)-1):
#             a=nums[i+1]-nums[i]
#             res=max(a,res)
#         return res

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i - 1])
        return res