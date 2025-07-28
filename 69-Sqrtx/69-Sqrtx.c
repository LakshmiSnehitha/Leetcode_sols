// Last updated: 7/28/2025, 3:30:36 PM
int mySqrt(int n){
    long long  i;
    long long low=1;
    long long high= n;
    while(low<=high)
    {
      
       while(low<=high)
       {
            long long  mid=low+high>>1;
           if(mid*mid==n)
           {
               return mid;
           }
           else if (mid*mid<n)
           {
            low=mid+1;
           }
           else
            high=mid-1;
       }

    }
    return high;
}
