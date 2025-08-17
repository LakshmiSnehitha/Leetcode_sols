# Last updated: 8/17/2025, 2:19:21 PM
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s=sorted(nums)
        s1=s[::-1]
    
        if(nums==s or nums==s1):
            return True
        else:
            return False