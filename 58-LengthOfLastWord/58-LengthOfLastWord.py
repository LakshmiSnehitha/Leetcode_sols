# Last updated: 7/28/2025, 3:30:31 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.strip().split()
        return len(l[-1])
