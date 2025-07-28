// Last updated: 7/28/2025, 3:29:37 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
    int c=0;
    ListNode temp=head;
    while(temp!=null){
        c++;
        temp=temp.next;
    }
    temp=head;
    int m=c/2;
    while(m-->0){
        temp=temp.next;
    }
    return temp;
        
    }
}