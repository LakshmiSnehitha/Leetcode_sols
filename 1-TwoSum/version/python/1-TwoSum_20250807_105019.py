# Last updated: 8/7/2025, 10:50:19 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return (i,j)
               
     
        