# Last updated: 8/5/2025, 7:28:31 PM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        s=[]
        for i in range (len(nums)):
            if target == nums[i]:
                s.append(i)
        return s