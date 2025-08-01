# Last updated: 8/2/2025, 12:05:39 AM
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range (n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                        c=c+1
        return c

        