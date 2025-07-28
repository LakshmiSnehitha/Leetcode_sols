# Last updated: 7/28/2025, 3:30:30 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        l = []
        for i in digits:
            s = s*10+i
            x = s+1
            l = list(map(int,str(x)))
        return l        