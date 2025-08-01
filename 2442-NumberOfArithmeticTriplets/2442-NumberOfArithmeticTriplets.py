# Last updated: 8/2/2025, 12:05:45 AM
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s=set(nums)
        c=0
        for i in nums:
            if(i+diff in nums and i+2*diff in nums):
                c=c+1
        return c
