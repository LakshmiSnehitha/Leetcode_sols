// Last updated: 7/28/2025, 3:29:35 PM
class Solution {
public:
    bool divisorGame(int n) {
       if(n%2==0){
           n=n-1;
           return true;
       } 
       else{
           n=n-1;
           return false;
       }
    }
};