# Last updated: 8/1/2025, 1:19:40 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st=s.split()
        return ' '.join(st[:k])
