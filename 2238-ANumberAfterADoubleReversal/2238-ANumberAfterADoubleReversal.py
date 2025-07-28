# Last updated: 7/28/2025, 3:28:58 PM
class Solution:
    def reverse(n):
        rev=0
      
        while(n!=0):
            r=n%10
            rev=rev*10+r
            n=n//10
        return rev
    def isSameAfterReversals(self, num: int) -> bool:
        rev1=Solution.reverse(num)
        rev2=Solution.reverse(rev1)
        return rev2==num

