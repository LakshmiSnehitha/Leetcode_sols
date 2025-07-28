// Last updated: 7/28/2025, 3:29:51 PM
int arrangeCoins(int n){
        long low = 1;
        long high = n;
        long mid=(low+high)>>1;
        while(low<=high){
        mid=(low+high)>>1;
        long a=(mid*(mid+1))/2;
        if (a==n)
        {
            return (int)mid;
        }
        else if(a<n)
        {
            low=mid+1;
        }
        else
        {
            high=mid-1;
        }
    }
    return (int)high;
}