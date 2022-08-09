# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None):
            return head
        n=1
        a=head
        while(a.next):
            a=a.next
            n+=1
        a.next=head
        for _ in range(n-k%n):
            a=a.next
        head=a.next
        a.next=None
        return head
        