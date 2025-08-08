# Last updated: 8/8/2025, 9:36:53 PM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=[]
        d=[]
        q=len(nums)
        for i in range (len(nums)):
            if nums[i]%2==0:
                s.append(nums[i])
            else:
                d.append(nums[i])
        return s+d
        