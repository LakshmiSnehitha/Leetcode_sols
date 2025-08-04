# Last updated: 8/4/2025, 7:24:33 PM
# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         d={}
#         for i in nums:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#          return sum(key for key, val in d.items() if val == 1)    
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # Now sum only the elements that appeared once
        return sum(key for key, val in d.items() if val == 1)
