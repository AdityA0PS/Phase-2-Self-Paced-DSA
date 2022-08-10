class Node:
    
    def __init__(self, key = 0, val = 0, freq = 1):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = self.prev = None
        
class Dllist:
    
    def __init__(self):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        self.len = 0
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} # { key : node }
        self.freqList = {}  # { freq : Dllist }
        self.cap = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            freq = node.freq
            curFreq = freq + 1
            
            # remove from prev list
            self.freqList[freq].remove(node)
            self.freqList[freq].len -= 1
            # add to new list
            node.freq = curFreq
            # build curFreq List
            if curFreq not in self.freqList:
                self.freqList[curFreq] = Dllist()
            self.freqList[curFreq].insert(node)
            self.freqList[curFreq].len += 1
            
            return node.val 
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        curFreq = 1
        if key in self.cache:
            node = self.cache[key]
            freq = node.freq
            curFreq = freq + 1
            self.freqList[freq].remove(node)
            self.freqList[freq].len -= 1
        elif len(self.cache) == self.cap:
            for i in range(1, len(self.freqList) + 1):
                # delete lfu node
                if self.freqList[i].len > 0:
                    lfu = self.freqList[i].left.next
                    self.freqList[i].remove(lfu)
                    self.freqList[i].len -= 1
                    del self.cache[lfu.key]
                    break
        
        node = Node(key, value, curFreq)
        # build curFreq List
        if curFreq not in self.freqList:
            self.freqList[curFreq] = Dllist()
        self.freqList[curFreq].insert(node)
        self.freqList[curFreq].len += 1
        self.cache[key] = node