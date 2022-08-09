"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None
        
        old_ptr = head.next
        cur_ptr = new_head = Node(head.val, None, None)
        address = {head:new_head}
        
        while old_ptr != None:
            address[old_ptr] = Node(old_ptr.val, None, None)
            cur_ptr.next = address[old_ptr]
            
            cur_ptr = cur_ptr.next
            old_ptr = old_ptr.next
            
        cur_ptr, old_ptr = new_head, head
        
        while cur_ptr != None:
            if old_ptr.random in address:
                cur_ptr.random = address[old_ptr.random]
                
            cur_ptr = cur_ptr.next
            old_ptr = old_ptr.next
            
        return new_head
        