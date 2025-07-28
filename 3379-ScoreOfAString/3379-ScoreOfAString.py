# Last updated: 7/28/2025, 3:28:44 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        e=0
        for i in range (len(s)-1):
            # d=abs(ord(s[i])-ord(s[i+1]))
            d = abs(ord(s[i]) - ord(s[i + 1]))
            e=e+d
        return e



        
        