/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    //ListNode* reverseKGroup(ListNode* head, int k) {
       ListNode* reverseKGroup(ListNode* head, int k) {
        if(!head) return head;
        
        ListNode* t = head;
        for(int i = 0; i < k; ++i){
            if(!t) return head;
            t = t->next;
        }
        
        ListNode* prev = NULL, *curr = head, *nex = head;
        int ct = 0;
        while(ct < k){
            nex = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nex;
            ct++;
        }
        if(nex) head->next = reverseKGroup(nex, k);
        return prev;  
    }
};