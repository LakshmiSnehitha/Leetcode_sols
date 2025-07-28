// Last updated: 7/28/2025, 3:30:45 PM
class Solution {
public:
    bool isPalindrome(long long x) {
        long long  rev=0;
        long long   t=x;
        int r;
        if(t<0){
            return false;
        }
        while(x!=0)
        {r=x%10;
        rev=rev*10+r;
        x/=10;

        }
        if(t==rev){
            return true;
        }
        else{
            return false;
        }
        
    }
};