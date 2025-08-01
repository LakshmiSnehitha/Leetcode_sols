// Last updated: 7/28/2025, 3:30:25 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head==NULL) return head;
    struct ListNode *temp = head;
    while(temp->next!=NULL){
        if(temp->val==temp->next->val){
            temp->next=temp->next->next;
        }
        else{
            temp=temp->next;
        }
    }
    return  head;
}