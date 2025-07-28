# Last updated: 7/28/2025, 3:30:02 PM
class Solution:
    ist=[]
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        d={}
        for i in nums:
            if i in d:
                return i
            d[i]=1
        return -1



        # for i in range (1,len(nums)):
        #     nums.sort()
        #     if nums[i]==nums[i-1]:
        #         return nums[i]
        #     return -1
        
            
        