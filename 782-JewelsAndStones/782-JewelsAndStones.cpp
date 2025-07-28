// Last updated: 7/28/2025, 3:29:38 PM
class Solution {
public:
    int numJewelsInStones(string jw, string st) {
        int c=0;
        for(int i=0;jw[i]!='\0';i++)
        {
            for(int j=0;st[j]!='\0';j++)
            {
                if(st[j]==jw[i])
                {
                     c+=1;
                }
            }
        }
    return c;
    }
};