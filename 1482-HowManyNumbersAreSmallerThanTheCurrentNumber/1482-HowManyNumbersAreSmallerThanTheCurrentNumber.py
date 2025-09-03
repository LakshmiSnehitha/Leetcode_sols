# Last updated: 9/3/2025, 11:24:34 AM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=[]
        for i in range (len(nums)):
            count=0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    count+=1
            c.append(count)
        return c
        