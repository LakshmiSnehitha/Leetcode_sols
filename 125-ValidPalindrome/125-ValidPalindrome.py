# Last updated: 7/28/2025, 3:30:24 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                s1=s1+i
        s1=s1.lower()
        print(s1)
        i=0
        j=len(s1)-1
        while(i<=j):
            if s1[i]!=s1[j]:
                return False
            i=i+1
            j=j-1
        return True
       

                

        