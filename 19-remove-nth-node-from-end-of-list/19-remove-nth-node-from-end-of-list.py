class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None if n==1 else head
        cur,k=head,0
        while cur is not None:
            k+=1
            cur=cur.next
        cur,k=head,k-n
        if k==0:
            head=head.next
        else:
            while cur is not None:
                k-=1
                if k==0:
                    break
                cur=cur.next
            cur.next=cur.next.next
        return head