// Last updated: 7/28/2025, 3:29:34 PM
class Solution {
public:
    int subtractProductAndSum(int n) {
        int s=0,p=1,r;
        int t=n;
        while(n!=0){
            r=n%10;
            s+=r;
            p*=r;
            n=n/10;
    

        }
        return p-s;
    }
};