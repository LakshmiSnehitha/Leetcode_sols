// Last updated: 7/28/2025, 3:29:05 PM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int c=0;
        for(int i=0;i<operations.size();i++)
        {
            if(operations[i]=="++X" || operations[i]=="X++")
            {
                c=c+1;
            }
            else{
        c=c-1;
            }
        }
        return c;
    }
};
