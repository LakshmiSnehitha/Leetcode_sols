# Last updated: 8/5/2025, 7:22:15 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        s=[]
        for i in range (len(words)):
            if  x in words[i]:
                s.append(i)
        return s

        