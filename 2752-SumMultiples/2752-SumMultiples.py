# Last updated: 7/31/2025, 10:45:45 AM
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s=0
        for i in range(1,n+1):
            if(i%3==0 or i%5==0 or i%7==0):
                s=s+i
        return s
        