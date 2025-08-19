# Last updated: 8/19/2025, 4:14:35 PM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d={}
        s=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value==2:
                s.append(key)
        return s
      