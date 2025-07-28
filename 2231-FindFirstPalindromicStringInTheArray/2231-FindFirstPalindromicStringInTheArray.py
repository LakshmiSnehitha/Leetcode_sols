# Last updated: 7/28/2025, 3:29:00 PM
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        l=[]
        for i in words:
            if i==i[::-1]:
                l.append(i)
        if l:
            return l[0]
        else:
            return ""

            
              