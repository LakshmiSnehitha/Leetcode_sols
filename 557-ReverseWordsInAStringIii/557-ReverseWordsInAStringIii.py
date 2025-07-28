# Last updated: 7/28/2025, 3:29:48 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        a=[]
        for i in d:
            p=i[::-1]
            a.append(p)
        return ' '.join(a)
        # a=[i[::-1]for i in d]
        # return ' '.join(a)
     
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split()  # Split sentence into words
#         reversed_words = [word[::-1] for word in words]  # Reverse each word
#         return ' '.join(reversed_words)  # Join them back into a string
 