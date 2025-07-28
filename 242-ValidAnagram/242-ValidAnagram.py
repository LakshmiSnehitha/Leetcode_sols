# Last updated: 7/28/2025, 3:30:07 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        if(s1==t1):
            return True
        else:
            return False