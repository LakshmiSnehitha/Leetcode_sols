# Last updated: 7/31/2025, 9:56:20 PM
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        org=x

        while(x>0):
            s+=x%10
            x=x//10
        if(org%s==0):
            return s
        else:
            return -1