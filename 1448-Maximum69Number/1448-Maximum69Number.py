# Last updated: 8/17/2025, 2:19:09 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        return int(n.replace('6','9',1))
        