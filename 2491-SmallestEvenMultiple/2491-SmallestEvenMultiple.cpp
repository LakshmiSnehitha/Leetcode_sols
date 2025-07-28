// Last updated: 7/28/2025, 3:28:50 PM
class Solution {
public:
    int smallestEvenMultiple(int n) {
        int c=0;
        for(int i=1;i<=2;i++)
        {
            int x=n*i;
            if(x%2==0 && x%n==0)
            {c+=x;
            break;

            }
        }
        return c;
    }
};