# Last updated: 8/3/2025, 5:14:16 PM
# class Solution:
#     def countTriples(self, n: int) -> int:
#         cnt=0
#         for a in range (1,n+1):
#             for b in range(1,n+1):
#                 for c in range(1,n+1):
#                     if((a*a)+(b*b)==(c*c)):
#                         cnt+=1
#         return cnt
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                if c <= n and c * c == c_squared:
                    count += 1
        return count

        