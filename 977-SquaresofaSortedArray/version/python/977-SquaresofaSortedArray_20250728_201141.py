# Last updated: 7/28/2025, 8:11:41 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums:
            s.append(i*i)
        return sorted(s)  