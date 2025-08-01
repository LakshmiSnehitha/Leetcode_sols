# Last updated: 8/1/2025, 9:42:41 AM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(n):
            r=sum(nums[:i])
            l=sum(nums[i+1:])
            a.append(abs(l-r))
        return a