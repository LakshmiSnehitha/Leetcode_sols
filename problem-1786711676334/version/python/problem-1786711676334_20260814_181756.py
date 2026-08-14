# Last updated: 8/14/2026, 6:17:56 PM
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        b=[]
4        for i in str(n):
5            if i !='0':
6                b.append(int(i))
7        c= sum(b)
8        num=0
9        for i in b:
10            num= num*10+i
11        return num*c
12
13        