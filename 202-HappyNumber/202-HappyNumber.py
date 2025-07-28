# Last updated: 7/28/2025, 3:30:14 PM
class Solution:
    def perfect(n):
        s=0
        while(n!=0):
            r=n%10
            s+=r*r
            n=n//10
        return s
    def isHappy(self, n: int) -> bool:
        while(n>9):
            n=Solution.perfect(n)
        return n==1 or n==7













        # l=0
        # sum=0
        # while n>0:
        #     l=n%10
        #     sum=sum+ l*l
        #     n=n//10
        # if sum==1:
        #     return True
        # elif sum==7:return True #only one happy number(7) b/w 1 and 10
        # elif sum<10: return False
        # else:
        #     return self.isHappy(sum)       