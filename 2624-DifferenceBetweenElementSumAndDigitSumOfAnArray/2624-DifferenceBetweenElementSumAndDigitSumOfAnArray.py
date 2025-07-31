# Last updated: 7/31/2025, 9:56:25 PM
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        m=0
        for i in nums:
            while i > 0:
                m=m+i%10
                i=i//10
        return abs(s-m)
        