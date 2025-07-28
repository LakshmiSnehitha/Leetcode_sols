// Last updated: 7/28/2025, 3:30:19 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *a=headA;
    struct ListNode *b= headB;
    while(a!=b)
    {
        a=a==NULL? headB:a->next;
        b=b==NULL?  headA:b->next;
    }
    return a;


}