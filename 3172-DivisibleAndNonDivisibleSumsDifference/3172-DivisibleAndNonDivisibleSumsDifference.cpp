// Last updated: 7/28/2025, 3:28:42 PM
class Solution {
public:
    int differenceOfSums(int n, int m) {
        int i,c1=0,c2=0;
        for(i=1;i<=n;i++)
        {
            if(i%m!=0)
            {
                c1+=i;

            }
            else{
                c2+=i;
              
            }
        }
        
       int d=c1-c2;
   return d;
    }
};