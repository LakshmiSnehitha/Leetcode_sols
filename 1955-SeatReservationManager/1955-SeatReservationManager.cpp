// Last updated: 7/28/2025, 3:29:12 PM
class SeatManager {
public:
priority_queue<int,vector<int>,greater<int>>pq;
    SeatManager(int n) {
        for(int i=1;i<=n;i++)
        {
            pq.push(i);
        }
    }
    
    int reserve() {
        int res=pq.top();
        pq.pop();
        return res;
    }
    
    void unreserve(int seatNumber) {
        pq.push(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */