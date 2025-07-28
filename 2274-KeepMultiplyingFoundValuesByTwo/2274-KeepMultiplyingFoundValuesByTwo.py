# Last updated: 7/28/2025, 3:28:57 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s=set(nums)
        while(original in s):
            original*=2
        return original
        # for i in nums:
        #     if i in original:
        #         s=i*2
        #     return s

        