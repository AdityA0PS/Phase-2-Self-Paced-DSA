class Node:
    def __init__(self, key: int , val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key : node
        
        # init double linked list
        self.head, self.tail = Node(0, 0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left


    def insert(self, node):
        left = self.tail.prev
        left.next = node
        node.prev = left
        node.next = self.tail
        self.tail.prev = node
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            
        else:
            node = Node(key, value)
            if self.cap == len(self.cache):
                firstNode = self.head.next
                del self.cache[firstNode.key]
                self.remove(firstNode)
                
            self.insert(node)
            self.cache[key] = node