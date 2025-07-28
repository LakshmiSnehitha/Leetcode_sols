# Last updated: 7/28/2025, 3:28:55 PM
class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=0
            while(i>0):
                n=i%10
                s=s+n
                i=i//10
            if(s%2==0):
                c+=1
        return c
                
       