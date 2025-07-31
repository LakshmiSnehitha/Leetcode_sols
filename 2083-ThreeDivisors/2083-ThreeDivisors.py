# Last updated: 7/31/2025, 9:56:35 PM
class Solution:
    def isThree(self, n: int) -> bool:
        c=0
        for i in range(1,n+1):
            if(n%i==0):
                c+=1
        return c==3