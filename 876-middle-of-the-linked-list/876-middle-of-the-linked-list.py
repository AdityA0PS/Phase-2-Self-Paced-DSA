class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        itr = head
        listt = []
        while itr:
            listt.append(itr)
            itr = itr.next
        return listt[len(listt)//2]