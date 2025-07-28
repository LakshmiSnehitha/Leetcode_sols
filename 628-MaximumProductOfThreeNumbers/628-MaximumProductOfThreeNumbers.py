# Last updated: 7/28/2025, 3:29:44 PM
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        d=nums[-1]*nums[-2]*nums[-3]
        d1=nums[0]*nums[1]*nums[-1]
        return max(d,d1)
             