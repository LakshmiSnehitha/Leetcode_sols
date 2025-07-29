# Last updated: 7/30/2025, 12:12:40 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums:
            s.append(i*i)
        return sorted(s)  