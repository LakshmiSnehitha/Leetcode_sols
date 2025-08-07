# Last updated: 8/7/2025, 11:06:47 AM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        c=0
        for i in range (len(nums)):
            for j in range(i+1,n):
                if nums[i]+nums[j]<target:
                    c+=1
        return c

        