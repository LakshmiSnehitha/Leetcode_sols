# Last updated: 7/28/2025, 3:29:57 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dis={}
        for i in s:
            if i in dis:
                dis[i]+=1
            else:
                dis[i]=1
        for l in range(len(s)):
             if dis[s[l]] == 1:
                return l
        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # Step 1: Count frequency of each character
#         count = {}
#         for char in s:
#             if char in count:
#                 count[char] += 1
#             else:
#                 count[char] = 1

#         # Step 2: Find the index of the first unique character
#         for i in range(len(s)):
#             if count[s[i]] == 1:
#                 return i
#         return -1
