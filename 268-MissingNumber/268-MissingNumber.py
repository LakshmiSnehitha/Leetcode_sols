# Last updated: 7/28/2025, 3:30:04 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)#3
        for i in range (len(nums)):#[3,0,1] len 3
            res+=(i-nums[i])#i=3,0,1 -1 2 3
        return res
            

             
         