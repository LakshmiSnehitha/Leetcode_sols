# Last updated: 7/28/2025, 3:30:05 PM
# class Solution:
#     def addDigits(self, num: int) -> int:
#         s=0
#         while(num!=0):
#             r=num%10
#             s=s+r
#             num=num//10
#         if(num==0  and s>=10):
#             num= s  
#          
#         return num     
        
class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num > 0: 
            r = num % 10
            s += r # s = 11
            num = num // 10 # n = 11
            if num == 0 and s >= 10:
                num = s
                s = 0
        return s