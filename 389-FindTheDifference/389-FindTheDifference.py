# Last updated: 7/28/2025, 3:29:55 PM
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         s1=[]
#         t1=[]
#         for i in range(len(s)):
#             s1.append(ord(i))
#         for j in range(len(t)):
#             t1.append(ord(j))
#         return abs(s1-t1)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(c) for c in s)
        t_sum = sum(ord(c) for c in t)
        return chr(t_sum - s_sum)
