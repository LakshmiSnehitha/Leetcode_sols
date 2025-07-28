// Last updated: 7/28/2025, 3:29:32 PM
class Solution {
public:
    int heightChecker(vector<int>& heights) {
       int c=0;
       vector<int> arr1=heights;
       sort(heights.begin(),heights.end()) ;
       for(int i=0;i<arr1.size();i++)
       {
        if(heights[i]!=arr1[i])
        {
            c++;
        }
       }
       return c;
    }
};