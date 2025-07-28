# Last updated: 7/28/2025, 3:29:20 PM
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        n = len(d)
        for j in sorted(d.values()):
            k-=j
            if(k<0):
                return n
            else:
                n-=1
        return n