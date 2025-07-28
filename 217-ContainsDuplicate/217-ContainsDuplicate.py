# Last updated: 7/28/2025, 3:30:10 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=set()
        for i in nums:
            if(i in num):
                return True
            num.add(i)
        
        return False
        