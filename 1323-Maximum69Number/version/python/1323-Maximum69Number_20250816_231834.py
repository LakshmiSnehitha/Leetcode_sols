# Last updated: 8/16/2025, 11:18:34 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        return int(n.replace('6','9',1))
        