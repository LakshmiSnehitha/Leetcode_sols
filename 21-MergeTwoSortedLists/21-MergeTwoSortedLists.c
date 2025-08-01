// Last updated: 7/28/2025, 3:30:43 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 // in recursion
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
struct ListNode *result;
    if(l1==NULL) return l2;
    if(l2==NULL) return l1;
    if(l1->val <= l2->val)
    {
        result=l1;
        result->next=mergeTwoLists(l1->next,l2);
    }
    else{
        result=l2;
        result->next=mergeTwoLists(l1,l2->next);
    }
    return  result;
}